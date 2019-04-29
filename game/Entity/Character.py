from Entity.Entity import Entity
from Entity.Characteristic import *

class Character(Entity):

    def __init__(self, name, worldPath, characs, dialogue, color = "\u001b[36m"):
        Entity.__init__(self, name, worldPath)
        self.characteristics = characs
        self.dialogues = dialogue
        self.color = color

    def load(self, lines):
        pass

    def toFile(self):
        self.remove()
        self.writeIn("class "+self.name+":")

        self.writeIn("\tdef __init__(self):")

        if self.characteristics:
            for perk in self.characteristics:
                self.writeIn(perk.toString())

        self.writeIn("\t\tself.dialogue = "+str(self.dialogues))

        self.writeIn("\n")

        self.writeIn("\tdef talk(self,saidToHim):")

        if not self.dialogues:
            self.writeIn("\n\npass")
        else:
            self.writeIn("\t\tif not self.dialogue:")
            self.writeIn("\t\t\tprint(\"*Fait des gestes avec ses bras*\")")
            self.writeIn("\t\t\tprint(\"Ce personnage ne peut apparemment pas parler.\")")
            self.writeIn("\t\t\treturn")
            self.writeIn("\t\tthinkingAbout = self.dialogue")
            self.writeIn("\t\tnext = self.dialogue")
            self.writeIn("\t\tfor listensTo in saidToHim:")
            self.writeIn("\t\t\tthinkingAbout = next[listensTo]")
            self.writeIn("\t\t\tnext = thinkingAbout[1]")
            self.writeIn("\t\tprint(u\""+self.color+self.name+":\u001b[37m \", end = '')")
            self.writeIn("\t\tfor line in thinkingAbout[0].split('\\n'):")
            self.writeIn("\t\t\tprint(u\"\u001b[37m\"+line)")
            self.writeIn("\t\t\tprint(\"\\n\")")
            self.writeIn("\t\tprint(\"\\n\")")
            self.writeIn("\t\tr = 1")
            self.writeIn("\t\tfor choice,reponses in thinkingAbout[1].items():")
            self.writeIn("\t\t\tprint(str(r)+\": \"+choice  )")
            self.writeIn("\t\t\tr += 1")
