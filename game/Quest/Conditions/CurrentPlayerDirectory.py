import sys
sys.path.append("..")
from Quest.Condition import Condition
from Command.Command import Command
import os

# Example for a simple condition.
# Such structure will allow human readable quest conditions in config files

# example:
# Quest-example.quest
# name: "Create a rock in the parc"
# onStart: none
# onResolve: none
# steps: []
# conditions: [EntityExists(Rock("/Parc"))]

class CurrentPlayerDirectory(Condition):
    def __init__(self, path):
        self.path = path.replace("\\","/")
        pass

    def met(self):
        print(os.getcwd().replace(Command.game.root,''))
        return os.getcwd().replace(Command.game.root,'').replace("\\","/") == self.path

    def printItself(self):
        super()
        print(":CurrentPlayerDirectory")
