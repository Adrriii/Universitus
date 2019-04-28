import sys
sys.path.append("..")
from Quest.Event import Event
from Entity.Character import *

class CreateCharacter(Event):
    def __init__(self, charac):
        self.charac = charac
        pass

    def do(self):
        self.charac.toFile()

    def printItself(self):
        super()
        print(":CreateCharacter")
