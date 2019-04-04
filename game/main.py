#!/usr/bin/python3
import os
from Game import *

game = Game()

for title,quest in game.quests.items():
    print(title+": ")
    print(quest.evalConditions())

os.chdir("world")
game.root = os.getcwd()
os.chdir("Parc")
game.start()

