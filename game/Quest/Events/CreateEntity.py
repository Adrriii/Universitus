import sys
sys.path.append("..")
from Quest.Event import Event
from Entity.Entity import Entity

class CreateEntity(Event):
    def __init__(self, entity):
        self.entity = entity
        pass

    def do(self):
        self.entity.create()

    def printItself(self):
        super()
        print(":CreateEntity")
