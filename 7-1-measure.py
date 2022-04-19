import RPi.GPIO
import time
import matplotlib.pyplot as plot

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
comp = 4
troyka = 17
st = 0.005
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(dac, RPi.GPIO.OUT)
RPi.GPIO.setup(leds, RPi.GPIO.OUT)
RPi.GPIO.setup(troyka, RPi.GPIO.OUT)
RPi.GPIO.setup(comp, RPi.GPIO.IN)

def dec2bin(n):
    RPi.GPIO.output(leds, [int(j) for j in bin(n)[2:].zfill(8)])


def adc():
    j = [int(j) for j in bin(0)[2:].zfill(8)]
    for i in range(8):
        j[i] = 1
        RPi.GPIO.output(dac, j)
        time.sleep(st)
        if RPi.GPIO.input(comp) == 0:
            j[i] = 0
        RPi.GPIO.output(leds, j)
    return (j[0]*128+j[1]*64+j[2]*32+j[3]*16+j[4]*8+j[5]*4+j[6]*2+j[7])*3.3/256


try:
    meas = []
    t0 = time.time()
    RPi.GPIO.output(troyka, 1)
    while True:
        p = adc()
        if p<3.2:
            meas.append(p)
            print(p)
        else:
            break
    RPi.GPIO.output(troyka, 0)
    while True:
        p = adc()
        if p>0.066:
            meas.append(p)
            print(p)
        else:
            break
    t1 = time.time()
    t01 = t1 - t0
    plot.plot(meas)
    plot.show()
    with open("data.txt", "w") as out:
        out.write("\n".join([str(i) for i in meas]))
        freq = t01 / len(meas)
        step = 3.3 / 256
        fr = 1 / st
        print(t01)
        print(freq)
        print(st)
        print(step)
    with open("settings.txt", "w") as sets:
        sets.write(str(st)+'\n'+str(step))
finally:
    RPi.GPIO.output(dac, 0)
    RPi.GPIO.output(troyka, 0)
    RPi.GPIO.cleanup()
