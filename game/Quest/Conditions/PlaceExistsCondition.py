import sys
sys.path.append("..")
from Quest.Condition import Condition

class PlaceExistsCondition(Condition):
    def __init__(self):
        pass

    def met(self):
        return True # system call to check a folder

    def printItself(self):
        print("PlaceExistsCondition")
