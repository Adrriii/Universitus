import os
import subprocess
from io import StringIO

class Command:

    root = '' # world root, initialized by the game

    def __init__(self):
        pass

    def perform(self, args):
        output = subprocess.check_output(args)
        return output

    def inbounds(self, path):
        full = os.path.abspath(path)
        return Command.root in full

class cd(Command):

    def perform(self, args):
        try:
            destination = args[1]
            try:
                if(self.inbounds(destination)):
                    os.chdir(args[1])
                else:
                    print("You are not allowed to go there")
            except:
                print("You cannot go to \""+destination+"\"")
        except:
            print("Invalid destination")

class ls(Command):
    pass

class pwd(Command):
    pass

class touch(Command):
    pass

class echo(Command):
    pass

class python(Command):
    pass
class edit(Command):

    def perform(self, args):
        try:
            destination = args[1]
            try:
                if(self.inbounds(destination)):
                    with open(args[1],mode='r') as f:
                        return bytes(f.read(), 'utf-8')
            except:
                print("You cannot edit \""+destination+"\"")
        except:
            print("Invalid file")