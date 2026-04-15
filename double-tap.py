import RPi.GPIO as gpio
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

gpio.setmode(gpio.BCM)

sleep_time = 0.2
num = 0

up_but   = 9
down_but = 10
gpio.setup(up_but,   gpio.IN)
gpio.setup(down_but, gpio.IN)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
gpio.setup(leds, gpio.OUT)
gpio.output(leds, 0)

while True:
    if gpio.input(up_but):
        if num == 3:
            num -= 1
        num += 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    if gpio.input(down_but):
        if num == 0:
            num += 1
        num -= 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    if gpio.input(down_but) and gpio.input(up_but):
        num = 255
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    gpio.output(leds, dec2bin(num))
