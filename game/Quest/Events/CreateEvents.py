import sys
import os
sys.path.append("..")
from Quest.Event import Event
from Entity.Entity import Entity

class CreateLock(Event):
    def __init__(self, path, message="Cet endroit est verrouillé."):
        self.path = path
        self.message = message
        pass

    def do(self):
        with open(self.path+"/.lock", 'w') as f:
            f.write(self.message)

    def printItself(self):
        super()
        print(":CreateLock")

class CreateEntity(Event):
    def __init__(self, entity):
        self.entity = entity
        pass

    def do(self):
        self.entity.create()

    def printItself(self):
        super()
        print(":CreateEntity")

class CreateCharacter(Event):
    def __init__(self, charac):
        self.charac = charac
        pass

    def do(self):
        self.charac.toFile()

    def printItself(self):
        super()
        print(":CreateCharacter")