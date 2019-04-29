import sys
sys.path.append("..")
from Quest.Event import Event
from Command.Command import Command

class AppendDialogueChoice(Event):
    def __init__(self, npc, dialogue):
        self.npc = npc
        self.dialogue = dialogue
        pass

    def met(self):
        return Command.game.dialogues.append(self.dialogue)

    def printItself(self):
        super()
        print(":AppendDialogueChoice")
