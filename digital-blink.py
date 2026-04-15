import RPi.GPIO as gpio
import time

led    = 26
state  = 0
period = 0.2
button = 13

gpio.setmode(gpio.BCM)
gpio.setup(led,    gpio.OUT)
gpio.setup(button, gpio.IN)

while True:
    if gpio.input(button):
        state = not state
        gpio.output(led, state)
        time.sleep(period)