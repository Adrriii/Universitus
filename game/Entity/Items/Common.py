import sys
sys.path.append("..")
from Entity.Entity import Entity

class Rock(Entity):
    def __init__(self, worldPath):
        Entity.__init__(self,worldPath, "Rock")
        pass

class Paper(Entity):
    def __init__(self, worldPath):
        Entity.__init__(self,worldPath, "Paper")
        pass

class Scissors(Entity):
    def __init__(self, worldPath):
        Entity.__init__(self,worldPath, "Scissors")
        pass