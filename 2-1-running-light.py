import RPi.GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(leds, RPi.GPIO.OUT)
for j in range(3):
    for i in leds:
        RPi.GPIO.output(i, 1)
        time.sleep(0.2)
        RPi.GPIO.output(i, 0)
RPi.GPIO.output(leds, 0)
RPi.GPIO.cleanup()
