from Entity.Entity import Entity
from Entity.Characteristic import *

class Character(Entity):

    def __init__(self, name, worldPath, characs):
        Entity.__init__(self, name, worldPath)
        self.characteristics = characs

    def load(self, lines):
        pass

    def toFile(self):
        self.remove()
        self.writeIn("class Personnage:")
        self.writeIn("    def __init__(self):")
        for perk in self.characteristics:
            self.writeIn(perk.toString())
