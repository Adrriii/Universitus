import os
import subprocess
import importlib
from io import StringIO

class Command:

    game = None # Access to the game

    def __init__(self):
        pass

    def perform(self, args):
        output = subprocess.check_output(args, shell=True)
        return output

    def inbounds(self, path):
        full = os.path.abspath(path)
        return os.path.abspath(self.game.root+"/") in full

class cd(Command):

    def perform(self, args):
        try:
            destination = args[1]
            try:
                if(self.inbounds(destination)):
                    os.chdir(args[1])
                    if(os.path.isfile(".lore")):
                        with open(".lore",'r') as f:
                            for line in f.readlines():
                                sprint(line, end = '')
                            sprint("\n")
                else:
                    sprint("Impossible d'aller ici.")
            except:
                sprint("Vous ne pouvez pas vous diriger vers \""+destination+"\"")
        except:
            sprint("Cette destination est invalide.")

class cat(Command):

    def perform(self, args):
        try:
            destination = args[1]
            try:
                if(self.inbounds(destination)):
                    super.perform(args)
                else:
                    sprint("Impossible de voir ce qui se trouve à l'intérieur.")
            except:
                sprint("Cet endroit est inaccessible.")
        except:
            sprint("Cet objet est invalide.")

class ls(Command):
    pass

class pwd(Command):
    pass

class touch(Command):

    def perform(self, args):
        try:
            destination = args[1]
            try:
                if(self.inbounds(destination)):
                    open(destination,'a').close()
            except:
                sprint("Vous ne pouvez pas créer \""+destination+"\"")
        except:
            sprint("L'endroit auquel vous tentez d'accéder est incorrect.")

class talk(Command):

    def perform(self, args):
        try:
            destination = args[1]
            try:
                if(self.inbounds(destination)):
                    name = destination[:-3]
                    if(destination[-3:] == ".py"):
                        try:
                            with open(destination,'r', encoding="utf-8") as f:
                                text = ''.join(f.readlines())
                                exec(text)
                                character = eval(name+"()")

                                said = [""]
                                if(name in self.game.dialogues.keys()):
                                    # Continue talk
                                    said = self.game.dialogues[name]
                                    
                                    dialogueTree = character.dialogue
                                    next = character.dialogue
                                    for choice in said:
                                        dialogueTree = next[choice]
                                        next = dialogueTree[1]

                                    try:
                                        i = 1
                                        for choice,response in dialogueTree[1].items():
                                            if i == int(args[2]):
                                                said.append(choice)
                                                break
                                            i += 1
                                    except Exception as e:
                                        sprint("Choix invalide. ( "+str(e)+" )")
                                        return
                                        
                                self.game.dialogues[name] = said
                                character.talk(said)
                        except Exception as e:
                            sprint("*Bruits inintelligibles*")
                            sprint("Quelque chose ne va pas avec cette créature... ( "+str(e)+" )")
                    else:
                        sprint("Ceci ne peut parler !")
            except:
                sprint("Vous ne pouvez pas vous adresser à "+destination)
        except:
            sprint("La personne à qui vous tentez de vous adresser est hors de portée.")

class restart(Command):
    def perform(self, args):
        exit()

class edit_(Command):

    def perform(self, args):
        try:
            command = ' '.join(args)
            text = ('"'.join(('"'.join(command.split('"')[1:]).split('"'))[:-1])).replace('\\n','\n')
            f_out = os.path.abspath(command.split(">")[-1].strip())

            try:
                
                if(self.inbounds(f_out)):
                    with open(f_out, 'w') as f:
                        f.write(text)
                else:
                    sprint("Vous ne pouvez pas modifier cet objet.")
            except:
                sprint("Vous ne pouvez pas modifier cet objet")
        except:
            sprint("L'objet que vous tentez de modifier est invalide.")

class python(Command):
    pass
class edit(Command):

    def perform(self, args):
        try:
            destination = args[1]
            try:
                if(self.inbounds(destination)):
                    with open(args[1],mode='r') as f:
                        return bytes(f.read(), 'utf-8')
            except:
                sprint("Vous ne pouvez pas modifier cet objet.")
        except:
            sprint("L'objet que vous tentez de modifier est invalide.")