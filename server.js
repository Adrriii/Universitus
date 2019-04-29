"use strict";
let Stream = require('stream')
let Docker = require('dockerode')
let docker = new Docker({ socketPath: '/var/run/docker.sock' })
let moduleDocker = require('./moduleDocker');

const data_manager = require('./data_manager');

console.log("Connecting to mysql server ...");
const dm = new data_manager();

// Port where we'll run the websocket server
var webSocketsServerPort = 1337;

// websocket and http servers
var webSocketServer = require('websocket').server;
var http = require('http');

/**
 * Global variables
 */
// list of currently connected clients (users)
var clients = [];
// list of users' state (see enum)
var clients_status = [];

let status = {
    INIT: 0,
    LOGIN: 1,
    REGISTER: 2,
    CONFIRM: 3,
    GAME: 4,
}

let containeurs = {};
/**
 * Helper function for escaping input strings
 */
function htmlEntities(str) {
    return String(str)
        .replace(/&/g, '&amp;').replace(/</g, '&lt;')
        .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}



function sendMessage(index, text, password = false) {
    let obj = {
        time: (new Date()).getTime(),
        text: text,
        author: "",
        color: false,
        password: password
    };

    let json = JSON.stringify({
        type: 'message',
        data: obj
    });

    clients[index].sendUTF(json);
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

    // potentially initialize the client
    if (!clients_status[index]) {
        clients_status[index] = 0;
    }

    var userName = false;

    console.log((new Date()) + ' Connection accepted.');

    // user sent some message
    connection.on('message', function (message) {
        if (message.type === 'utf8') { // accept only text
            // first message sent by user is their name

            switch (clients_status[index]) {
                case status.INIT:
                    // remember user name
                    userName = htmlEntities(message.utf8Data);

                    // Challenge username with the database
                    dm.getUserFromUsername(userName).then(rows => {
                        if (!rows || !rows.length) {
                            // New user
                            // Go in state 2 for registration
                            clients_status[index] = status.REGISTER;
                            sendMessage(index, "New Password for " + userName + " : ", true);
                        } else {
                            // Existing user, asking for identification
                            clients_status[index] = status.LOGIN;
                            sendMessage(index, "Password for " + userName + " : ", true);
                        }
                    });
                    break;
                case status.LOGIN:
                    // Check password and either connect (state 4) or simply retry.

                    dm.checkUserLogin(userName, message.utf8Data).then(
                        rows => {
                            if (rows.length) {
                                clients_status[index] = status.GAME;

                                // Temporary container, since saves don't work yet
                                // TODO : load user's save
                                createContainer(userName, index);
                            } else {
                                sendMessage(index, "<br>Wrong password. Try again.<br>",true);
                            }
                        }
                    )

                    break;
                case status.REGISTER:

                    // Check if the password is good and either ask for validation (state 3) or simply retry

                    clients_status[index] = status.CONFIRM;
                    sendMessage(index, "<br>Repeat Password : ", true);
                    break;
                case status.CONFIRM:
                    // Check if the password is good then either create the container and connect (state 4) or retry

                    dm.registerUser(userName, message.utf8Data).then(
                        rows => {
                            if (rows.insertId > 0) {
                                createContainer(userName, index);
                                clients_status[index] = status.GAME;
                            } else {
                                sendMessage(index, "<br>An error occured. Try again!<br>");
                                clients_status[index] = status.INIT;
                            }
                        }
                    )
                    break;
                case status.GAME:
                    containeurs[userName]['stdin'].write(message.utf8Data + "\n");
                    break;
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