import sys
sys.path.append("..")
from Quest.Condition import Condition
from Command.Command import Command
import os

class CurrentPlayerDirectory(Condition):
    def __init__(self, path):
        self.path = path.replace("\\","/")
        pass

    def met(self):
        return os.getcwd().replace(Command.game.root,'').replace("\\","/") == self.path

    def printItself(self):
        super()
        print(":CurrentPlayerDirectory")
