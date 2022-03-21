import RPi.GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(dac, RPi.GPIO.OUT)

def dec2bin(n):
    return [int(j) for j in bin(n)[2:].zfill(8)]


try:
    x = int(input())
    while True:
        for i in range(256):
            RPi.GPIO.output(dac, dec2bin(i))
            time.sleep(x/512)
        for i in range(255, 0, -1):
            RPi.GPIO.output(dac, dec2bin(i))
            time.sleep(x/512)
except ValueError:
    print('emergency, stopped')
finally:
    RPi.GPIO.output(dac, 0)
    RPi.GPIO.cleanup()
