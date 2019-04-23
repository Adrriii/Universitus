#!/usr/bin/python3
import os
import sys

directory = os.path.dirname(os.path.abspath(__file__))
 
while not directory.endswith('game'):
    directory = os.path.dirname(directory)
 
if directory not in sys.path:
    sys.path.append(directory)

from Player import *

player = Player()
print("C'est un chat")
player.say("Hello")