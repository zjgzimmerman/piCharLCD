#!/usr/bin/python3
from piCharLCD import piCharLCD

print("Initializing screen object")
screen = piCharLCD(13, 6, 5, [27, 17, 4, 26, 23, 24, 25])

print("Cleaning up GPIO")
screen.cleanup
