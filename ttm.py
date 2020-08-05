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

def letterA():
    dot(1)
    line(1)
def letterB():
    line(1)
    dot(3)
def letterC():
    line(1)
    dot(1)
    line(1)
    dot(1)
def letterD():
    line(1)
    dot(2)
def letterE():
    dot(1)
def letterF():
    dot(2)
    line(1)
    dot(1)
def letterG():
    line(2)
    dot(1)
def letterH():
    dot(4)
def letterI():
    dot(2)
def letterJ():
    dot(1)
    line(3)
def letterK():
    line(1)
    dot(1)
    line(1)
def letterL():
    dot(1)
    line(1)
    dot(2)
def letterM():
    line(2)
def letterN():
    line(1)
    dot(1)
def letterO():
    line(3)
def letterP():
    dot(1)
    line(2)
    dot(1)
def letterQ():
    line(2)
    dot(1)
    line(1)
def letterR():
    dot(1)
    line(1)
    dot(1)
def letterS():
    dot(3)
def letterT():
    line(1)
def letterU():
    dot(2)
    line(1)
def letterV():
    dot(3)
    line(1)
def letterW():
    dot(1)
    line(2)
def letterX():
    line(1)
    dot(2)
    line(1)
def letterY():
    line(1)
    dot(1)
    line(2)
def letterZ():
    line(2)
    dot(2)


dict = {"a": letterA,
        "b": letterB,
        "c": letterC,
        "d": letterD,
        "e": letterE,
        "f": letterF,
        "g": letterG,
        "h": letterH,
        "i": letterI,
        "j": letterJ,
        "k": letterK,
        "l": letterL,
        "m": letterM,
        "n": letterN,
        "o": letterO,
        "p": letterP,
        "k": letterK,
        "r": letterR,
        "s": letterS,
        "t": letterT,
        "u": letterU,
        "v": letterV,
        "w": letterW,
        "x": letterX,
        "y": letterY,
        "z": letterZ,
    }

def morse(text):
    for x in text:
        dict[x]()
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
