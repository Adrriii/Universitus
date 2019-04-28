#!/usr/bin/python3

import os
from Game import *
import os

DEBUG = True

game = Game() 

os.chdir("world")
game.root = os.getcwd()+"/"

print("Message de bienvenue")

while(True):
    try:
        game.start()
    except Exception as e:
        if DEBUG:
            raise e
        print("Restarting...")
