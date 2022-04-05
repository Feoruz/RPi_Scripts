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
    j = dec2bin(0)
    for i in range(8):
        j[i] = 1
        RPi.GPIO.output(dac, j)
        time.sleep(0.01)
        if RPi.GPIO.input(comp) == 0:
            j[i] = 0
    return j[0]*128+j[1]*64+j[2]*32+j[3]*16+j[4]*8+j[5]*4+j[6]*2+j[7]
    

try:
    while True:
        print(adc(), adc()*3.3/256)
finally:
    RPi.GPIO.output(dac, 0)
    RPi.GPIO.output(troyka, 0)
    RPi.GPIO.cleanup()
