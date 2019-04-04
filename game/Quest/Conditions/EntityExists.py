import sys
sys.path.append("..")
from Quest.Condition import Condition

# Example for a simple condition.
# Such structure will allow human readable quest conditions in config files

# example:
# Quest-example.quest
# name: "Create a rock in the parc"
# onStart: none
# onResolve: none
# steps: []
# conditions: [EntityExists(Rock("/Parc"))]

class EntityExists(Condition):
    def __init__(self, entity):
        self.entity = entity
        pass

    def met(self):
        return self.entity.exists()

    def printItself(self):
        print("EntityExists")
