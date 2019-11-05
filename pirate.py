#!/usr/bin/python3

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import random

from gpiozero import MotionSensor

import subprocess

import os
import random

#print choose_file()

pir = MotionSensor(17)

pixel_pin = board.D12

num_pixels = 1

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.6, auto_write=False,
                           pixel_order=ORDER)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)

def choose_file():

    path ='/home/pi/scripts/pirate/sounds/'
    files = os.listdir(path)
    index = random.randrange(0, len(files))

    return files[index]


def clear_pixels():

    pixels.fill((0,0,0))
    pixels.show()

def colour_pixels(colour):

    pixels.fill(wheel(colour))
    pixels.show()

def caught():

    global risk_level

    colour_pixels(10)
    subprocess.call(["aplay", "/home/pi/scripts/pirate/sounds/"+choose_file()])
    time.sleep(2)
    risk_level=0
    clear_pixels()

subprocess.Popen(["aplay", "/home/pi/scripts/pirate/449939__x3nus__pirate-s-bounty.wav"])

for i in range (0,255):

    colour_pixels(i)
    time.sleep(.1)

subprocess.Popen(["aplay", "/home/pi/scripts/pirate/401931__qalba4j__piratematt-1.wav"])

clear_pixels()

risk_level=0

TRIGGER_THRESHOLD=9
#time between motion check
TIME_INTERVAL=0.3


while True:

#check motion and change risk level

    if pir.motion_detected:

        risk_level+=1

    else:

        risk_level-=1

#keep risk level at or above 0

    if risk_level<=0:

        risk_level=0

    print (risk_level)

    if risk_level==TRIGGER_THRESHOLD:

        caught()

    else:pass

    time.sleep(TIME_INTERVAL)





