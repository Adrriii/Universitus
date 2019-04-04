import os

from Player import *
from Quest.Quest import *
from Command.Command import *
from Entity.Items.Common import *

player = Player()

class Game :

    root = ''

    def __init__(self) :

        self.prefix = ["Parc"]
        self.user_name = "TOTO"
        self.quests = {}

        for subdir, dirs, files in os.walk("Quests"):
            for file in files:
                ext = os.path.splitext(file)[-1].lower()
                if ext == ".quest":
                    self.quests[file[:-6]] = Quest(file)

    def start(self) :

        path_place = self.prefix[0]

        while(True):
            input_string = input(self.user_name + "@:" + os.getcwd().replace(self.root,'') + "$ ")
            args = input_string.split(' ')

            try:
                command_string = args[0]
                try:
                    command = eval(command_string+"()")

                    command.perform(args)
                except:
                    print("Unknown command \""+command_string+"\"")
            except:
                pass