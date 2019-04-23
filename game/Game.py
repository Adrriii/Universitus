import os

from Player import *

player = Player()

class Game :

    def __init__(self) :

        self.path_base = "world/Parc/"
        self.path_place = ""
        self.prefix = []
        self.user_name = "TOTO"
        self.nb_place_append = 0


    def tick(self) :

        self.path_place = self.path_base

        while(True):

            input_string = input(self.user_name + "@:" + self.path_place + "$ ")
            
            self.nb_place_append = 0

            input_array = input_string.split(" && ")

            for input_string in input_array:

                input_string = self.parse_input(input_string)

                input_string = self.build_input(input_string)

                if(os.system(input_string) != 0):
                    for i in range(self.nb_place_append):
                        self.prefix.pop()


    def parse_input(self, input_string):

        if (input_string.startswith("cd")):

            input_string = self.cd(input_string)

        else:

            input_string = " && " + input_string

        return input_string


    def build_input(self, input_string):

        self.path_place = self.path_base
                
        for place in self.prefix:
            self.path_place += place + "/"
        
        return "cd " + self.path_place + input_string


    def cd(self, input_string):

        path = (input_string.split(" ")[1]).split("/")

        for place in path:

            if(place == ".."):
                if(len(self.prefix) > 0):
                    self.prefix.pop()
            else:
                self.prefix.append(place)
                self.nb_place_append += 1

        return ""

            