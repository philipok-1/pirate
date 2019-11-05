import subprocess

import os
import random

def choose_file():

    path ='/home/pi/scripts/pirate/sounds/'
    files = os.listdir(path)
    index = random.randrange(0, len(files))

    return files[index]

#print choose_file()

subprocess.call(["aplay", "/home/pi/scripts/pirate/sounds/"+choose_file()])
