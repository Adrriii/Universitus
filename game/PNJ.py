class PNJ :

    def __init__(self, name) :

        self.name = name
        self.conversation = []


    def append_text(self, text):

        self.conversation.append(text)

    def reply(self, reply_number = 0) :

        print(self.conversation[reply_number])


    def start_conversation(self) :
        
        reply_number = 0

        while(reply_number < len(self.conversation)):
            self.reply(reply_number)
            input("^")
            reply_number += 1


    def parse_command(self, argv):

        if(len(argv) < 2):
            pass
        else:
            if(argv[1] == "talk" or argv[1] == "t"):
                self.start_conversation()

