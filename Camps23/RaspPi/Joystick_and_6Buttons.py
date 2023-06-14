
"""
Example/Instructor Code for the "Shoebox Fightpad"

This code is completed and will perform all the inteded tasks of the fightpad, and for demo pursposes
may want to split up secions of the code or replace it.

In some cases this may be commented in a section and will be noted

Author: Connor Dawson
Last Updated: June 14, 2023


REQUIRED HARDWARE:
- 6 Buttons, for the fightpad use arcade style
- 1 joystick_, for the fightpad use arcade style
- 1 Raspberry Pi Pico
- 1 Breadboard
- 100-150in of wire
"""

import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#Define our keyboard for easier use later
kbd = Keyboard(usb_hid.devices)


# Define the GPIO pins for joystick_ inputs

joystick_up = board.GP8
joystick_down = board.GP11
joystick_left = board.GP10
joystick_right = board.GP9
#Define the GPIO pins for the 6 buttons

button1 = board.GP18
button2 = board.GP19
button3 = board.GP20
button4 = board.GP21
button5 = board.GP22
button6 = board.GP26

'''
Set the pins for joystick and button as digital input and as pull up resistors
The logic that will be used later reflects the pull up resistor choice made now, however using pull
down resistors should work, the logic would just need to be flipped.
'''

input_up = digitalio.DigitalInOut(joystick_up)
input_up.direction = digitalio.Direction.INPUT
input_up.pull = digitalio.Pull.UP

input_down = digitalio.DigitalInOut(joystick_down)
input_down.direction = digitalio.Direction.INPUT
input_down.pull = digitalio.Pull.UP

input_left = digitalio.DigitalInOut(joystick_left)
input_left.direction = digitalio.Direction.INPUT
input_left.pull = digitalio.Pull.UP

input_right = digitalio.DigitalInOut(joystick_right)
input_right.direction = digitalio.Direction.INPUT
input_right.pull = digitalio.Pull.UP

input_button1 = digitalio.DigitalInOut(button1)
input_button1.direction = digitalio.Direction.INPUT
input_button1.pull = digitalio.Pull.UP

input_button2 = digitalio.DigitalInOut(button2)
input_button2.direction = digitalio.Direction.INPUT
input_button2.pull = digitalio.Pull.UP

input_button3 = digitalio.DigitalInOut(button3)
input_button3.direction = digitalio.Direction.INPUT
input_button3.pull = digitalio.Pull.UP

input_button4 = digitalio.DigitalInOut(button4)
input_button4.direction = digitalio.Direction.INPUT
input_button4.pull = digitalio.Pull.UP

input_button5 = digitalio.DigitalInOut(button5)
input_button5.direction = digitalio.Direction.INPUT
input_button5.pull = digitalio.Pull.UP

input_button6 = digitalio.DigitalInOut(button6)
input_button6.direction = digitalio.Direction.INPUT
input_button6.pull = digitalio.Pull.UP

'''
Main loop to read joystick_ and button inputs
We use a while true loop here as we want to always be looking for the inputs from these peripherals
If at any point this loop stopped, the fightpad would no longer be functional
This is a common practice in hardware/embedded development however typically not ideal in software development
'''

while True:
    if not input_up.value: # We use inverse logic here as we have set the pull up resistors earlier
        kbd.press(Keycode.W) 
        # this will map the left movement of the joystick to the "W" key or could make it a arrow key with Keycode.RIGHT_ARROW
        print("joystick Up") # Print statement to check if it worked
        time.sleep(0.25) # Sleep to prevent debouncing
        # Debouncing is the act of preventing a button from activating multiple times in succession,
        # which often causes unintened use

    # We repeat this process for every direction on the joystick and every button
    # Any keys can be used but basic "WASD" and 1-6 are used in this example

    if not input_down.value:
        kbd.press(Keycode.A)
        print("joystick Down")
        time.sleep(0.25)

    if not input_left.value:
        kbd.press(Keycode.S)
        print("joystick Left")
        time.sleep(0.25)

    if not input_right.value:
        kbd.press(Keycode.D)
        print("joystick Right")
        time.sleep(0.25)

    if not input_button1.value:
        kbd.press(Keycode.ONE)
        print("Button 1 Pressed")
        time.sleep(0.25)

    if not input_button2.value:
        kbd.press(Keycode.TWO)
        print("Button 2 Pressed")
        time.sleep(0.25)

    if not input_button3.value:
        kbd.press(Keycode.THREE)
        print("Button 3 Pressed")
        time.sleep(0.25)

    if not input_button4.value:
        kbd.press(Keycode.FOUR)
        print("Button 4 Pressed")
        time.sleep(0.25)

    if not input_button5.value:
        kbd.press(Keycode.FIVE)
        print("Button 5 Pressed")
        time.sleep(0.25)

    if not input_button6.value:
        kbd.press(Keycode.SIX)
        print("Button 6 Pressed")
        time.sleep(0.25)

    