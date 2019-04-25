import os
import subprocess
from io import StringIO

class Command:

    root = '' # world root, initialized by the game

    def __init__(self):
        pass

    def perform(self, args):
        output = subprocess.check_output(args, shell=True)
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

    def perform(self, args):
        try:
            destination = args[1]
            try:
                if(self.inbounds(destination)):
                    open(destination,'a').close()
            except:
                print("You cannot edit \""+destination+"\"")
        except:
            print("Invalid destination")

class restart(Command):
    def perform(self, args):
        exit()

class edit_(Command):

    def perform(self, args):
        try:
            command = ' '.join(args)
            text = ('"'.join(('"'.join(command.split('"')[1:]).split('"'))[:-1])).replace('\\n','\n')
            f_out = os.path.abspath(command.split(">")[-1].strip())

            try:
                
                if(self.inbounds(f_out)):
                    with open(f_out, 'w') as f:
                        f.write(text)
                        print("Wrote to "+f_out)
                else:
                    print("You are not allowed to go edit this file")
            except:
                print("You cannot edit \""+f_out+"\"")
        except Exception as e:
            print("Invalid file ("+str(e)+")")

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