import RPi.GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(leds, RPi.GPIO.OUT)
RPi.GPIO.setup(aux, RPi.GPIO.IN)
while True:
    for i in range(8):
        RPi.GPIO.output(leds[i], RPi.GPIO.input(aux[i]))
RPi.GPIO.output(leds, 0)
RPi.GPIO.cleanup()
