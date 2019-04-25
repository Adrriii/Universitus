import sys
sys.path.append("..")
from Quest.Event import Event

class RemoveEntity(Event):
    def __init__(self, entity):
        pass

    def do(self):
        return True # system call to remove an entity

    def printItself(self):
        super()
        print(":RemoveEntity")
