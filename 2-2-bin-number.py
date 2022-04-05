import RPi.GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [1, 0, 1, 0, 1, 0, 1, 0]
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(dac, RPi.GPIO.OUT)
RPi.GPIO.output(dac, number)
time.sleep(15)

RPi.GPIO.output(dac, 0)
RPi.GPIO.cleanup()
