import os

from Player import *
from Quest.Quest import *
from Command.Command import *
from Entity.Items.Common import *

player = Player()

class Game :

    root = ''

    def __init__(self) :
        self.user_name = "Player"
        self.quests = {}
        self.activeQuests = {}

        for subdir, dirs, files in os.walk("Quests"):
            for file in files:
                ext = os.path.splitext(file)[-1].lower()
                if ext == ".quest":
                    self.quests[file[:-6]] = Quest(file)

    def startQuest(self, name):
        print("Started a new quest : "+name+" !")
        quest = self.quests[name]
        quest.start()
        self.activeQuests[name] = quest

    def checkQuests(self):
        toDelete = []

        for name, quest in self.activeQuests.items():
            resolved,nextQuests = quest.tryResolve()
            if resolved:
                print("Completed quest : "+name+" !")
                toDelete.append(name)

            for nextQuest in nextQuests:
                self.startQuest(nextQuest)
        
        for quest in toDelete:
            del self.activeQuests[quest]

    def start(self) :
        Command.root = self.root

        # If needed, replay all quests
        self.startQuest("rock")

        while(True):
            input_string = input(self.user_name + "@:" + os.getcwd().replace(self.root,'') + "$ ")
            args = input_string.split(' ')

            command_string = args[0]

            if(command_string != "setup"):
                try:
                    command = eval(command_string+"()")

                    output = command.perform(args)
                    if(output):
                        print(output.decode("utf-8"))
                except Exception as e:
                    print("Unknown command \""+command_string+"\"")

                self.checkQuests()
            else:
                if(args[1] == "nick"):
                    self.user_name = args[2]
                else:
                    print("Unknown command \""+command_string+"\"")