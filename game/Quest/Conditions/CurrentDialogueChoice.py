import sys
sys.path.append("..")
from Quest.Condition import Condition
from GetGame import GetGame
import os

class CurrentDialogueChoice(Condition):
    def __init__(self, npc, dialogue):
        self.npc = npc
        self.dialogue = dialogue
        pass

    def met(self):
        if not self.npc in GetGame.game.dialogues:
            return False
        return GetGame.game.dialogues[self.npc] == self.dialogue

    def printItself(self):
        super()
        print(":CurrentDialogueChoice")
