import sys
sys.path.append("..")
from Quest.Event import Event
from Entity.Entity import Entity
from Command.Command import *

class NpcToPlayer(Event):
    def __init__(self, name, said):
        self.name = name
        self.said = said
        pass

    def do(self):
        cmd = talk()
        if self.said == [""]:
            cmd.perform(["talk",self.name+".py"])
        else:
            cmd.perform(["talk",self.name+".py",self.said])

    def printItself(self):
        super()
        print(":NpcToPlayer")
