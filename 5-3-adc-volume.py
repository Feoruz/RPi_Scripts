import RPi.GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(dac, RPi.GPIO.OUT)
RPi.GPIO.setup(leds, RPi.GPIO.OUT)
RPi.GPIO.setup(troyka, RPi.GPIO.OUT, initial=RPi.GPIO.HIGH)
RPi.GPIO.setup(comp, RPi.GPIO.IN)

def dec2bin(n):
    return [int(j) for j in bin(n)[2:].zfill(8)]


def adc():
    j = dec2bin(0)
    for i in range(8):
        j[i] = 1
        RPi.GPIO.output(dac, j)
        time.sleep(0.005)
        if RPi.GPIO.input(comp) == 0:
            j[i] = 0
    return j[0]*128+j[1]*64+j[2]*32+j[3]*16+j[4]*8+j[5]*4+j[6]*2+j[7]
    

try:
    while True:
        f = adc()
        print(f, f*3.3/256)
        g = dec2bin(0)
        for i in range(round(f/32)):
            g[i] = 1
        RPi.GPIO.output(leds, g)
finally:
    RPi.GPIO.output(dac, 0)
    RPi.GPIO.output(leds, 0)
    RPi.GPIO.output(troyka, 0)
    RPi.GPIO.cleanup()
