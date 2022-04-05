import RPi.GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(dac, RPi.GPIO.OUT)
RPi.GPIO.setup(troyka, RPi.GPIO.OUT, initial=RPi.GPIO.HIGH)
RPi.GPIO.setup(comp, RPi.GPIO.IN)

def dec2bin(n):
    return [int(j) for j in bin(n)[2:].zfill(8)]


def adc():
    for i in range(256):
        RPi.GPIO.output(dac, dec2bin(i))
        time.sleep(0.01)
        if RPi.GPIO.input(comp) == 0:
            return i

    

try:
    while True:
        f = adc()
        print(f, f*3.3/256)
finally:
    RPi.GPIO.output(dac, 0)
    RPi.GPIO.output(troyka, 0)
    RPi.GPIO.cleanup()
