# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Button and LED example for Pico. Turns on LED when button is pressed.

REQUIRED HARDWARE:
* Button switch on pin GP13.
* LED on pin GP14.
"""

#joystick1 = digitalio.DigitalInOut(board.GP8)

#joystick1.switch_to_input(pull = digitalio.Pull.DOWN)

#joystick2 = digitalio.DigitalInOut(board.GP9)
#joystick2.switch_to_input(pull = digitalio.Pull.DOWN)

#joystick3 = digitalio.DigitalInOut(board.GP10)
#joystick3.switch_to_input(pull = digitalio.Pull.DOWN)

#joystick4 = digitalio.DigitalInOut(board.GP11)
#joystick4.switch_to_input(pull = digitalio.Pull.DOWN)

import board
import digitalio
import time

# Define the GPIO pins for joystick inputs
pin_up = board.GP8
pin_down = board.GP11
pin_left = board.GP10
pin_right = board.GP9
pin_button1 = board.GP18
pin_button2 = board.GP19
pin_button3 = board.GP20
pin_button4 = board.GP21
pin_button5 = board.GP22
pin_button6 = board.GP26

# Set the pins as digital input
input_up = digitalio.DigitalInOut(pin_up)
input_up.direction = digitalio.Direction.INPUT
input_up.pull = digitalio.Pull.UP

input_down = digitalio.DigitalInOut(pin_down)
input_down.direction = digitalio.Direction.INPUT
input_down.pull = digitalio.Pull.UP

input_left = digitalio.DigitalInOut(pin_left)
input_left.direction = digitalio.Direction.INPUT
input_left.pull = digitalio.Pull.UP

input_right = digitalio.DigitalInOut(pin_right)
input_right.direction = digitalio.Direction.INPUT
input_right.pull = digitalio.Pull.UP

# Set the button as digital input
input_button1 = digitalio.DigitalInOut(pin_button1)
input_button1.direction = digitalio.Direction.INPUT
input_button1.pull = digitalio.Pull.UP

input_button2 = digitalio.DigitalInOut(pin_button2)
input_button2.direction = digitalio.Direction.INPUT
input_button2.pull = digitalio.Pull.UP

input_button3 = digitalio.DigitalInOut(pin_button3)
input_button3.direction = digitalio.Direction.INPUT
input_button3.pull = digitalio.Pull.UP

input_button4 = digitalio.DigitalInOut(pin_button4)
input_button4.direction = digitalio.Direction.INPUT
input_button4.pull = digitalio.Pull.UP

input_button5 = digitalio.DigitalInOut(pin_button5)
input_button5.direction = digitalio.Direction.INPUT
input_button5.pull = digitalio.Pull.UP

input_button6 = digitalio.DigitalInOut(pin_button6)
input_button6.direction = digitalio.Direction.INPUT
input_button6.pull = digitalio.Pull.UP


# Main loop to read joystick and button inputs
while True:
    if not input_up.value:
        print("Joystick Up")
        time.sleep(0.25)
    if not input_down.value:
        print("Joystick Down")
        time.sleep(0.25)
    if not input_left.value:
        print("Joystick Left")
        time.sleep(0.25)
    if not input_right.value:
        print("Joystick Right")
        time.sleep(0.25)
    if not input_button1.value:
        print("Button 1 Pressed")
        time.sleep(0.25)
    if not input_button2.value:
        print("Button 2 Pressed")
        time.sleep(0.25)
    if not input_button3.value:
        print("Button 3 Pressed")
        time.sleep(0.25)
    if not input_button4.value:
        print("Button 4 Pressed")
        time.sleep(0.25)
    if not input_button5.value:
        print("Button 5 Pressed")
        time.sleep(0.25)
    if not input_button6.value:
        print("Button 6 Pressed")
        time.sleep(0.25)

    




'''
while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)

    
    print("Joystick 1: ", joystick1.value)
    print("Joystick 2: ",joystick2.value)
    print("Joystick 3: ", joystick3.value)
    print("Joystick 4: ", joystick4.value, "\n")
    time.sleep(1)
    '''