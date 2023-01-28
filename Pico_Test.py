"""
Pico Intro Demo
Author: Connor
Date: Jan 27, 2023
"""


print("Hello World")

#Example for Pico. Turns the built-in LED on.
#Import the two required libraries to have access to the RP Pico pins
import board
import digitalio

#Set the onboard LED to output
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

#Turn on the LED
while True:
    led.value = True