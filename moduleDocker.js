function launchListCommandRec(docker, imageName, argsList, index) {
    if (index > argsList.length) {
        return;
    }

    docker.run(imageName, ['bash', '-c', argsList[index]], process.stdout)
    .then(container => {
        launchListCommandRec(docker, imageName, argsList, index + 1);
    })
}

module.exports = {
    create: (docker) => {
        return docker.createContainer({
            Image: 'ubuntu',
            AttachStdin: false,
            AttachStdout: true,
            AttachStderr: true,
            Tty: true,
            Cmd: ['/bin/bash'],
            OpenStdin: false,
            StdinOnce: false
        })
    },


    exec: (container, cmd) => {
            var options = {
                Cmd: ['bash', '-c', cmd],
                Env: [],
                AttachStdout: true,
                AttachStderr: true
            };

            container.exec(options, function (err, exec) {
                if (err) return;
                exec.start(function (err, stream) {
                    if (err) return;

                    container.modem.demuxStream(stream, process.stdout, process.stderr);

                    exec.inspect(function (err, data) {
                        if (err) return;
                        console.log(data);
                    });
                });
            });

    },


    launchCommand: (docker, imageName, cmd) => {
        docker.run(imageName, ['bash', '-c', cmd], process.stdout)
        // .then(container => {
        //     console.log(container.output.StatusCode);
        // })
    },

    launchListCommand: (docker, imageName, argsList) => {
        if (argsList.length == 0) {
            return;
        }

        launchListCommandRec(docker, imageName, argsList, 0);
    }
}