#!/usr/bin/python3
import os
import sys

directory = os.path.dirname(os.path.abspath(__file__))
 
while not directory.endswith('game'):
    directory = os.path.dirname(directory)
 
if directory not in sys.path:
    sys.path.append(directory)

from PNJ import *


cat = PNJ("Azrael")
cat.append_text("Hey ! J'aime manger des petits trucs bleus.")
cat.append_text("Et je vais te bouffer.")
cat.parse_command(sys.argv)