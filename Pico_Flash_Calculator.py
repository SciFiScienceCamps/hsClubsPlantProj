"""
Pico Flash Calculator
Author: Connor
Date: Jan 27, 2023
"""
#Example for Pico. Operates an addition calculator and blinks as many times as the output
#Import the two required libraries to have access to the RP Pico pins, and time
import board
import digitalio
import time
#Board setup and variable declaration
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
counter = 0
print("Welcome to the Addition Light Show!")
while True:

    #Take user input
    print("First Input")
    first_input = input()
    print("Second Input")
    second_input = input()
    #Sum user input
    result = int(first_input) + int(second_input)
    #if user sum larger than 99 try again
    if result >= 99:
        print("That will take too long, try something smaller!\n")
    else:
        #print the result
        print(result)
        #loop until the result = counter
        while counter <= result:
            #Blink the LED
            led.value = True
            time.sleep(0.5)
            if led.value == True:
                counter += 1
            print("The LED has flashed", counter, "times")
            led.value = False
            time.sleep(0.5)
