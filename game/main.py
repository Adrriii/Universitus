#!/usr/bin/python3
import os
from Game import *

game = Game() 

os.chdir("world")
game.root = os.getcwd()
os.chdir("Parc")

print("Message de bienvenue")

while(True):
    try:
        game.start()
    except:
        print("Something unexpected happened, sorry ! Restarting...")
