#!/usr/bin/env python3
import os
import time
import pyfiglet

def dot(x):
    dot_sound = lambda duration = 0.1, freq = 950 : os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    for i in range(x):
        dot_sound()

def line(x):
    line_sound = lambda duration = 0.3, freq = 950 : os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    for i in range(x):
        line_sound()

def morse(text):
    for x in text:
        if x == "a":
            dot(1)
            line(1)
        elif x == "b":
            line(1)
            dot(3)
        elif x == "c":
            line(1)
            dot(1)
            line(1)
            dot(1)
        elif x == "d":
            line(1)
            dot(2)
        elif x == "e":
            dot(1)
        elif x == "f":
            dot(2)
            line(1)
            dot(1)
        elif x == "g":
            line(2)
            dot(1)
        elif x == "h":
            dot(4)
        elif x == "i":
            dot(2)
        elif x == "j":
            dot(1)
            line(3)
        elif x == "k":
            line(1)
            dot(1)
            line(1)
        elif x == "l":
            dot(1)
            line(1)
            dot(2)
        elif x == "m":
            line(2)
        elif x == "n":
            line(1)
            dot(1)
        elif x == "o":
            line(3)
        elif x == "p":
            dot(1)
            line(2)
            dot(1)
        elif x == "q":
            line(2)
            dot(1)
            line(1)
        elif x == "r":
            dot(1)
            line(1)
            dot(1)
        elif x == "s":
            dot(3)
        elif x == "t":
            line(1)
        elif x == "u":
            dot(2)
            line(1)
        elif x == "v":
            dot(3)
            line(1)
        elif x == "w":
            dot(1)
            line(2)
        elif x == "x":
            line(1)
            dot(2)
            line(1)
        elif x == "y":
            line(1)
            dot(1)
            line(2)
        elif x == "z":
            line(2)
            dot(2)
        time.sleep(0.5)

welcome = pyfiglet.figlet_format("Text To Morse")
print(welcome)
print("mail: ben3sta@protonmail.com")
print("")
print('---Type "/exit" to exit')
print("")
while True:
    text = (input("Text: ")).lower()
    if text == "/exit":
        break
    else:
        morse(text)
