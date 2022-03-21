import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(22, RPi.GPIO.OUT)

try:
    p = RPi.GPIO.PWM(22, 2)
    p.start(0)
    x = int(input())
    p.ChangeDutyCycle(x)
    x = input()
    p.stop()
finally:
    RPi.GPIO.cleanup()
