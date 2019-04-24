import os

from Player import *

player = Player()

class Game :

    def __init__(self) :

        self.path_base = "world"
        self.path_place = ""
        self.prefix = ["Parc"]
        self.user_name = "TOTO"
        self.nb_place_append = 0
        self.inventory = "Inventaire"
        self.inventory_shortcut = "i"
        self.place_save_path = []


    def tick(self) :

        self.path_place = self.path_base
        self.path_place += "/" + self.prefix[0] + "/"

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
                    self.path_place = self.path_base
                
                    self.path_place += "/"

                    for place in self.prefix:
                        self.path_place += place + "/"


    def parse_input(self, input_string):

        if (input_string.startswith("cd")):

            input_string = self.cd(input_string)

        else:

            input_string = " && " + input_string

        return input_string


    def build_input(self, input_string):

        self.path_place = self.path_base
                
        self.path_place += "/"

        for place in self.prefix:
            self.path_place += place + "/"
        
        return "cd " + self.path_place + input_string


    def cd(self, input_string):

        path = input_string.split(" ")

        if(len(path) <= 1):
            return ""

        path = path[1].split("/")

        for place in path:

            print(place)

            if(place == self.inventory or place == self.inventory_shortcut):

                for place in self.prefix:
                    self.place_save_path.append(place)

                for place in self.place_save_path:
                    self.prefix.pop()

                self.prefix.append(self.inventory)
                self.nb_place_append += 1

            elif(place == ".."):

                if(self.prefix[len(self.prefix) - 1] == self.inventory):
                    
                    self.prefix.pop()

                    for place_saved in self.place_save_path:
                        
                        self.prefix.append(place_saved)
                        self.nb_place_append += 1

                    for i in range (len(self.place_save_path)):
                        self.place_save_path.pop()

                elif(len(self.prefix) > 1):
                    self.prefix.pop()
            else:
                self.prefix.append(place)
                self.nb_place_append += 1

        return ""

            