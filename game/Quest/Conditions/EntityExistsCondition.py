import * from Condition

# Example for a simple condition.
# Such structure will allow human readable quest conditions in config files

# example:
# Quest-example.quest
# name: "Create a rock in the parc"
# onStart: none
# onResolve: none
# steps: []
# conditions: [EntityExistsCondition(Rock("/Parc"))]

class EntityExistsCondition(Condition):
    def __init__(self, entity):
        self.entity = entity
        pass

    def met():
        return entity.exists()