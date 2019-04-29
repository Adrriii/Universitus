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

class SetDialogueChoice(Event):
    def __init__(self, npc, dialogues):
        self.npc = npc
        self.dialogues = dialogues
        pass

    def met(self):
        return Command.game.dialogues = self.dialogues

    def printItself(self):
        super()
        print(":SetDialogueChoice")
        
class NpcToPlayer(Event):
    def __init__(self, name, said):
        self.name = name
        self.said = said
        pass

    def do(self):
        cmd = talk()
        Command.game.dialogues[self.name] = self.said
        cmd.perform(["talk",self.name+".py"])

    def printItself(self):
        super()
        print(":NpcToPlayer")
