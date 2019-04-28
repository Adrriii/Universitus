import os

from Player import *
from Quest.Quest import *
from Command.Command import *
from Entity.Items.Common import *

player = Player()

class Game :

    root = ''

    forbiddenCommands = ["help"]

    def __init__(self) :
        self.user_name = "Player"
        self.quests = {}
        self.activeQuests = {}
        self.dialogues = {}

        for subdir, dirs, files in os.walk("Quests"):
            for file in files:
                ext = os.path.splitext(file)[-1].lower()
                if ext == ".quest":
                    self.quests[file[:-6]] = Quest(file)

    def startQuest(self, name):
        quest = self.quests[name]
        print(u"\u001b[35mNouvelle quête : \u001b[0m"+quest.name)
        print(quest.description)
        print("\n")
        quest.start()
        self.activeQuests[name] = quest

    def checkQuests(self):
        toDelete = []
        toStart = []

        for name, quest in self.activeQuests.items():
            resolved,nextQuests = quest.tryResolve()
            if resolved:
                toDelete.append(name)

            for nextQuest in nextQuests:
                self.quests[nextQuest].setAvailable()
                toStart.append(nextQuest)
        
        for quest in toStart:
            self.startQuest(quest)
        
        for quest in toDelete:
            del self.activeQuests[quest]

    def start(self) :
        Command.game = self

        # Emulate user command to show lore example
        eval("cd()").perform(['cd',"Universitus"])

        # If needed, replay all quests
        self.quests["init"].setAvailable()
        self.startQuest("init")

        print("SYSTEM:username_request")

        while(True):
            input_string = input(self.user_name + "@:" + os.getcwd().replace(self.root,'') + "$ ")
            args = input_string.split(' ')

            command_string = args[0]

            if command_string in self.forbiddenCommands:
                print("Unknown command \""+command_string+"\"")
            else:
                if(command_string != "setup"):
                    try:
                        command = eval(command_string+"()")

                        output = command.perform(args)
                        if(output):
                            print(output.decode("utf-8"))
                    except Exception as e:
                        if(command_string == "restart"):
                            exit()
                        print("Unknown command \""+command_string+"\"")

                    self.checkQuests()
                else:
                    if(args[1] == "nick"):
                        self.user_name = args[2]
                    else:
                        print("Unknown command \""+command_string+"\"")
