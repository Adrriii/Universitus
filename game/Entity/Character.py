from Entity import Entity
from Entity.Characteristic import *

class Character(Entity) :

    def __init__(self, worldPath, name):
        super(worldPath, name)
        self.characteristics = []

    def load(self, lines):
        pass

    def toFile(self):
        for perk in self.characteristics:
            self.writeIn(perk.toString())
