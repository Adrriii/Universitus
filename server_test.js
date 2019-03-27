var Docker = require('dockerode');
let Stream = require('stream')
var fs = require('fs');
const util = require('util')

var socket = process.env.DOCKER_SOCKET || '/var/run/docker.sock';
var stats = fs.statSync(socket);

if (!stats.isSocket()) {
    throw new Error('Are you sure the docker is running?');
}






var docker = new Docker({
    socketPath: socket
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
    'Cmd': ['bash'],
    'Dns': ['8.8.8.8', '8.8.4.4'],
    'Image': 'ubuntu',
    'Volumes': {},
    'VolumesFrom': []
};

var previousKey,
    CTRL_P = '\u0010',
    CTRL_Q = '\u0011';

function handler(err, container,) {
    var attach_opts = {
        stream: true,
        stdin: true,
        stdout: true,
        stderr: true
    };

    return container.attach(attach_opts, (err, stream) => {
        // Show outputs
        process.stdin.pipe(stream);
        stream.on('data', function (key) {
            console.log("Receive data : " + key);

            if (previousKey === CTRL_P && key === CTRL_Q) exit(stream);
            previousKey = key;

            //console.log("Writing ls...");
            
            //stream.write("ls");
        });

        //What it does
        container.start(function (err, data) {
            container.wait(function (err, data) {
                exit(stream);
            });
        });
    });
}

// Exit container
function exit(stream) {
    //process.stdout.removeListener('resize', resize);
    //process.stdin.removeAllListeners();
    //process.stdin.setRawMode(isRaw);
    //process.stdin.resume();
    stream.end();
    process.exit();
}

let promiseCreation = docker.createContainer(optsc);



promiseCreation.then(container => {
    handler(1, container)
    
});
