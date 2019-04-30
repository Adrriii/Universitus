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
 * Base server on which the WebSocket server will run
 */
var server = http.createServer(function (request, response) {});
server.listen(webSocketsServerPort, function () {
    console.log((new Date()) + " Server is listening on port "
        + webSocketsServerPort);
});


/**
 * WebSocket server
 */
var wsServer = new webSocketServer({
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

async function createContainer(userName, index) {
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
                    
                    text = text.replace(/(\n)/g, '\\n');
                    sendMessage(index,text,false);
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
}

// This callback function is called every time someone
// tries to connect to the WebSocket server
wsServer.on('request', function (request) {
    console.log((new Date()) + ' Connection from origin ' + request.origin + '.');

    var connection = request.accept(null, request.origin);
    
    var index = clients.push(connection) - 1;

    // potentially initialize the client
    if (!clients_status[index]) {
        clients_status[index] = 0;
    }

    var userName = false;

    console.log((new Date()) + ' Connection accepted with index '+index);
    sendMessage(index, "Enter your login : ");

    // user sent some message
    connection.on('message', async function (message) {
        if (message.type === 'utf8') {

            switch (clients_status[index]) {
                case status.INIT:
                    // remember user name
                    userName = htmlEntities(message.utf8Data);

                    console.log((new Date()) + ' Username request : '+userName+'.');
                    // Challenge username with the database
                    await dm.getUserFromUsername(userName).then(rows => {
                        if (!rows || !rows.length) {
                            // New user
                            console.log((new Date()) + ' New user registering : '+userName+'.');
                            sendMessage(index, userName+"\\nNew Password for " + userName + " : ", true);
                            // Go in state 2 for registration
                            clients_status[index] = status.REGISTER;
                        } else {
                            // Existing user, asking for identification
                            console.log((new Date()) + " " + userName+" logging in.");
                            sendMessage(index, userName + "\\nPassword for " + userName + " : ", true);
                            clients_status[index] = status.LOGIN;
                        }
                    });
                    break;
                case status.LOGIN:
                    // Check password and either connect (state 4) or simply retry.
                    sendMessage(index, "\\n\\n");

                    await dm.checkUserLogin(userName, message.utf8Data).then(
                        rows => {
                            if (rows.length) {

                                // Temporary container, since saves don't work yet
                                // TODO : load user's save
                                createContainer(userName, index).then(function(v) {
                                    clients_status[index] = status.GAME;
                                });
                            } else {
                                sendMessage(index, "\\nWrong password. Try again.\n", true);
                            }
                        }
                    )

                    break;
                case status.REGISTER:

                    // Check if the password is good and either ask for validation (state 3) or simply retry

                    sendMessage(index, "\\nRepeat Password : ", true);
                    clients_status[index] = status.CONFIRM;
                    break;
                case status.CONFIRM:
                    // Check if the password is good then either create the container and connect (state 4) or retry
                    sendMessage(index, "\\n\\n");

                    await dm.registerUser(userName, message.utf8Data).then(
                        rows => {
                            if (rows.insertId > 0) {
                                console.log((new Date()) + " " + userName+" registered.");
                                createContainer(userName, index).then(function(v) {
                                    clients_status[index] = status.GAME;
                                });
                            } else {
                                sendMessage(index, "An error occured. Try again!\n");
                                clients_status[index] = status.INIT;
                            }
                        }
                    )
                    break;
                case status.GAME:
                    if(containeurs[userName]) {
                        containeurs[userName]['stdin'].write(message.utf8Data);
                    }
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
            clients_status.splice(index, 1);
        }
    });
});