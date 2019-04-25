#!/usr/bin/python3
import os
from Game import *

DEBUG = True

game = Game() 

os.chdir("world")
game.root = os.getcwd()
os.chdir("Parc")

print("Message de bienvenue")

while(True):
    try:
        game.start()
    except Exception as e:
        print("Restarting...")
        raise e
