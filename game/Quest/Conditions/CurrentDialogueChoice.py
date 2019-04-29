import sys
sys.path.append("..")
from Quest.Condition import Condition
from Command.Command import Command
import os

class CurrentDialogueChoice(Condition):
    def __init__(self, npc, dialogue):
        self.npc = npc
        self.dialogue = dialogue
        pass

    def met(self):
        return Command.game.dialogues[-1] == self.dialogue

    def printItself(self):
        super()
        print(":CurrentDialogueChoice")
