$(function () {
    "use strict";
    // for better performance - to avoid searching in DOM
    var content = $('#content');
    var input = $('#input');
    var terminal = $('#terminal');
    var textarea = $('#textarea');

    var buttonSave = $("input[name='buttonSave']");
    var buttonExit = $("input[name='buttonExit']");

    var taTitle = $('#textareaTitle');
    var taText = $('#textareaText');

    // my color assigned by the server
    var myColor = false;
    // my name sent to the server
    var myName = false;

    // if user is running mozilla then use it's built-in WebSocket
    window.WebSocket = window.WebSocket || window.MozWebSocket;

    // if browser doesn't support WebSocket, just show
    // some notification and exit
    if (!window.WebSocket) {
        content.html($('<p>', {
            text: 'Sorry, but your browser doesn\'t support this application.'
        }));
        input.hide();
        $('span').hide();
        return;
    }

    // open connection
    var connection = new WebSocket('ws://universitus.rhythmgamers.net:1337');
    //var connection = new WebSocket('ws://127.0.0.1:1337');



    connection.onopen = function () {
        // first we want users to enter their names
        input.removeAttr('disabled');
    };

    connection.onerror = function (error) {
        // just in there were some problems with connection...
        content.html($('<p>', {
            text: 'Sorry, but there\'s a problem with your ' +
                'connection or the server is down.'
        }));
    };

    // most important part - incoming messages
    connection.onmessage = function (message) {
        // try to parse JSON message. Because we know that the server
        // always returns JSON this should work without any problem but
        // we should make sure that the massage is not chunked or
        // otherwise damaged.
        try {
            var json = JSON.parse(message.data);
        } catch (e) {
            console.log('Invalid JSON: ', message.data);
            return;
        }

        // NOTE: if you're not sure about the JSON structure
        // check the server source code above
        // first response from the server with user's color
        if (json.type === 'color') {
            myColor = json.data;
            input.removeAttr('disabled').focus();
            // from now user can start sending messages
        } else if (json.type === 'history') { // entire message history
            // insert every single message to the chat window
            for (var i = 0; i < json.data.length; i++) {
                addMessage(json.data[i].author, json.data[i].text,
                    json.data[i].color, new Date(json.data[i].time));
            }
        } else if (json.type === 'message') { // it's a single message
            // let the user write another message
            input.removeAttr('disabled').focus();
            checkMessage(json.data.text);
            addMessage(json.data.author, json.data.text,
                json.data.color, new Date(json.data.time));
        } else {
            console.log('Hmm..., I\'ve never seen JSON like this:', json);
        }
    };

    /**
     * Send message when user presses Enter key
     */
    input.keydown(function (e) {
        if (e.keyCode === 13) {
            var msg = $(this).val();
            if (!msg) {
                return;
            }

            // send the message as an ordinary text
            connection.send(msg);
            $(this).val('');
            // disable the input field to make the user wait until server
            // sends back response
            input.attr('disabled', 'disabled');

            // we know that the first message sent from a user their name
            if (myName === false) {
                myName = msg;
            }
        }
    });

    /**
     * This method is optional. If the server wasn't able to
     * respond to the in 3 seconds then show some error message 
     * to notify the user that something is wrong.
     */
    setInterval(function () {
        if (connection.readyState !== 1) {
            input.attr('disabled', 'disabled').val(
                'Unable to communicate with the WebSocket server.');
        }
    }, 3000);

    /**
     * Check if message starts with edit:
     * Transition from terminal style window to a textarea
     */
    function checkMessage(message) {
        var line = message.split("\n");
        var pars = line[0].split(" ");
        // If the command is Edit, transition to text area window
        if (pars[0] == "edit" && pars.length <= 3) {
            terminal.attr('style', 'display: none');
            textarea.attr('style', 'display: block');
            taTitle.val(pars[1]);
        }
    }

    /**
     * Save button of the Edit Textarea
     */
    buttonSave.click(function () {
        var text = 'edit_ "' + taText.val() + '" > ' + taTitle.val();
        connection.send(text);

        terminal.attr('style', 'display: block');
        textarea.attr('style', 'display: none');
        taTitle.val('');
        taText.val('');
    });

    /**
     * Exit button of the Edit Textarea
     */
    buttonExit.click(function () {
        terminal.attr('style', 'display: block');
        textarea.attr('style', 'display: none');
        taTitle.val('');
        taText.val('');
    });

    /**
     * Add message to the chat window
     */
    function addMessage(author, message, color, dt) {
        content.append(message);
    }
});
