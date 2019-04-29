#!/usr/bin/python3
# coding=utf-8

import os
from Game import *
import os

def sprint(message, end = "\\n"):
    print(message,end)

DEBUG = True

game = Game() 

os.chdir("world")
game.root = os.getcwd()

while(True):
    try:
        game.start()
    except Exception as e:
        if DEBUG:
            raise e
        sprint("Restarting...")
