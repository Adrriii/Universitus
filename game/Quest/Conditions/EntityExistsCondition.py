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

class EntityExistsCondition(Condition):
    def __init__(self):
        pass

    def met(self):
        return entity.exists()

    def printItself(self):
        print("EntityExistsCondition")
