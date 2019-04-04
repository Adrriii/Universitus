import os

class Command:

    def __init__(self):
        pass

    def perform(self, args):
        output = os.system(" ".join(args))
        return output

class cd(Command):

    def perform(self, args):
        try:
            destination = args[1]
            try:
                os.chdir(args[1])
            except:
                print("You cannot go to \""+destination+"\"")
        except:
            print("Invalid destination")

class ls(Command):
    pass
    
class pwd(Command):
    pass