"use strict";
let Stream = require('stream')
let Docker = require('dockerode')
let Convert = require('ansi-to-html')
let docker = new Docker({ socketPath: '/var/run/docker.sock' })
let moduleDocker = require('./moduleDocker');

// used for formatting output into html
var convert = new Convert();

// Port where we'll run the websocket server
var webSocketsServerPort = 1337;

// websocket and http servers
var webSocketServer = require('websocket').server;
var http = require('http');

/**
 * Global variables
 */
// latest 100 messages
var history = [];
// list of currently connected clients (users)
var clients = [];

let containeurs = {};
/**
 * Helper function for escaping input strings
 */
function htmlEntities(str) {
    return String(str)
        .replace(/&/g, '&amp;').replace(/</g, '&lt;')
        .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

/**
 * HTTP server
 */
var server = http.createServer(function (request, response) {
    // Not important for us. We're writing WebSocket server,
    // not HTTP server
});
server.listen(webSocketsServerPort, function () {
    console.log((new Date()) + " Server is listening on port "
        + webSocketsServerPort);
});

// function exec(container, cmd) {

//     let s = new Stream.PassThrough();

//     var options = {
//         Cmd: ['bash', '-c', cmd],
//         Env: [],
//         AttachStdout: true,
//         AttachStderr: true
//     };
    
//     container.exec(options, function (err, exec) {
//         if (err) return;
//         exec.start(function (err, stream) {
//             if (err) return;
    
//             container.modem.demuxStream(stream, s, s);
    
//         });
//     });

//     return s;
// }


/**
 * WebSocket server
 */
var wsServer = new webSocketServer({
    // WebSocket server is tied to a HTTP server. WebSocket
    // request is just an enhanced HTTP request. For more info 
    // http://tools.ietf.org/html/rfc6455#page-6
    httpServer: server
});

var optsc = {
    'Hostname': '',
    'User': '',
    'AttachStdin': true,
    'AttachStdout': true,
    'AttachStderr': true,
    'Tty': true,
    'OpenStdin': true,
    'StdinOnce': false,
    'Env': null,
    'Cmd': [],
    'Dns': ['8.8.8.8', '8.8.4.4'],
    'Image': 'docker-game',
    'Volumes': {},
    'VolumesFrom': []
};

// This callback function is called every time someone
// tries to connect to the WebSocket server
wsServer.on('request', function (request) {
    console.log((new Date()) + ' Connection from origin ' + request.origin + '.');

    // accept connection - you should check 'request.origin' to
    // make sure that client is connecting from your website
    // (http://en.wikipedia.org/wiki/Same_origin_policy)
    var connection = request.accept(null, request.origin);
    // we need to know client index to remove them on 'close' event
    var index = clients.push(connection) - 1;
    var userName = false;

    console.log((new Date()) + ' Connection accepted.');

    // send back chat history
    if (history.length > 0) {
        connection.sendUTF(
            JSON.stringify({ type: 'history', data: history }));
    }

    // user sent some message
    connection.on('message', function (message) {
        if (message.type === 'utf8') { // accept only text
            // first message sent by user is their name

            if (userName === false) {
                // remember user name
                userName = htmlEntities(message.utf8Data);


                console.log("Creating containeur for " + userName + "...");
                docker.createContainer(optsc)
                    .then(container => {
                        containeurs[userName] = {
                            stdin: null,
                            stdout: null,
                            container_id: null
                        };

                        var attach_opts = {
                            stream: true,
                            stdin: false,
                            stdout: true,
                            stderr: false
                        };

                        containeurs[userName].container_id = container;

                        //stdout
                        container.attach(attach_opts, (err, stream) => {
                            
                            stream.on('data', key => {
                                var text = String(key);
                                if(text == "SYSTEM:username_request") {
                                    containeurs[userName]['stdin'].write("setup nick "+userName);
                                } else {
                                    if(text.substring(0,10) != "setup nick") {
                                        text = text.replace("\n","<br>")
        
                                        let obj = {
                                            time: (new Date()).getTime(),
                                            text: convert.toHtml(text),
                                            author: userName
                                        };
                                        
                                        let json = JSON.stringify({
                                            type: 'message',
                                            data: obj
                                        });
                                        clients[index].sendUTF(json);
                                    }
                                }
                            })
                        
                            console.log("Starting container...");
                            container.start()
                            .then(container => {
                                console.log("Containeur for " + userName + " succefully created and ready !");
                            })
                        });

                        var attach_opts = {
                            stream: true,
                            stdin: true,
                            stdout: false,
                            stderr: false
                        };

                        //stdin
                        container.attach(attach_opts, (err, stream) => {
                            containeurs[userName]['stdin'] = stream;
                        });
                    })


                connection.sendUTF(
                    JSON.stringify({
                        type: 'logged-in'
                    }));

                console.log((new Date()) + ' New user: ' + userName);
            } else {
                containeurs[userName]['stdin'].write(message.utf8Data);
            }
        }
    });

    // user disconnected
    connection.on('close', function (connection) {
        if (userName !== false) {
            console.log((new Date()) + " Peer "
                + connection.remoteAddress + " disconnected.");
            
            console.log("Removing container of " + userName);  
            containeurs[userName].container_id.stop()
            .catch(error => {
                //Container already stoped
            });

            console.log("Container succesfully removed !");
            

            // remove user from the list of connected clients
            clients.splice(index, 1);
        }
    });
});