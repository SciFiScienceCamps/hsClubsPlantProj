"""
Pico Flash Counter
Author: Connor
Date: Jan 27, 2023
"""

#Example for Pico. Flashes the built-in LED and counts every flash.
#Import the two required libraries to have access to the RP Pico pins, and time
import board
import digitalio
import time

#Board setup and variable declaration
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
counter = 0

while True:
    #Turn on the LED for .5 seconds
    led.value = True
    time.sleep(0.5)
    #Count up if it is on
    if led.value == True:
        counter += 1
    print("The LED has flashed", counter, "times") #Print the number of times it has flashed
    #Turn off the LED of .5 seconds
    led.value = False
    time.sleep(0.5)