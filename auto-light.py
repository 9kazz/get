import RPi.GPIO as gpio

state = 0
led   = 26
foto  = 6

gpio.setmode(gpio.BCM)
gpio.setup(led,  gpio.OUT)
gpio.setup(foto, gpio.IN)

while True:
    state = not gpio.input(foto)
    gpio.output(led, state)