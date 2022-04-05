import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(22, RPi.GPIO.OUT)

try:
    p = RPi.GPIO.PWM(22, 1000)
    x = float(input())
    p.start(x/3.3*100)
    #print("{:.2f}".format(3.3/100*x),' V')
    x = input()
    p.stop()
finally:
    RPi.GPIO.cleanup()
