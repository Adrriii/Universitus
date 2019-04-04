import os

from Player import *
from Quest.Quest import *
from Entity.Items.Common import *

player = Player()

class Game :

    def __init__(self) :

        self.prefix = ["Parc"];
        self.user_name = "TOTO"
        self.quests = {}

        for subdir, dirs, files in os.walk("Quests"):
            for file in files:
                ext = os.path.splitext(file)[-1].lower()
                if ext == ".quest":
                    self.quests[file[:-6]] = Quest(file)

    def tick(self) :

        path_place = self.prefix[0]

        while(True):
            input_string = input(self.user_name + "@:" + path_place + "$ ")
            #print(self.prefix)
            nb_place_append = 0

            if ("cd" in input_string):
                path = (input_string.split(" ")[1]).split("/")
                for place in path:
                    if(place == ".."):
                        self.prefix.pop()
                    else:
                        self.prefix.append(place)
                        nb_place_append += 1
                input_string = ""

            else:
                input_string = " && " + input_string

            path_place = ""
            for place in self.prefix:
                path_place += place + "/"
            #print(path_place)
            input_string = "cd " + path_place + input_string

            if(os.system(input_string) != 0):
                for i in range(nb_place_append):
                    self.prefix.pop()
