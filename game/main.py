#!/usr/bin/python3
# coding=utf-8

import os
from Game import *
import os

DEBUG = True

game = Game() 
game.user_name = "Player"

while(True):
    try:
        game.start()
    except Exception as e:
        if DEBUG:
            raise e
        print("Restarting...")
