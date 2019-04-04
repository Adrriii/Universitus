#!/usr/bin/python3
from Game import *

game = Game()

for title,quest in game.quests.items():
    print(title+": ")
    print(quest.evalConditions())

game.tick()

