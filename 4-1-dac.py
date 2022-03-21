import RPi.GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(dac, RPi.GPIO.OUT)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]


def isfloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def isint(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


try:
    while True:
        print('Number? uwu')
        x = input()
        if x == 'q':
            exit()
        elif not(isfloat(x)):
            print('integer required, you string appreciator')
        elif not(isint(x)):
            print('nxt time round is by urslf')
            x = round(float(x))
        else:
            x = int(x)
            if x > 255:
                print('too much!!! (<256 plz)')
            elif x < 0:
                print('>=0 plz')
            else:
                RPi.GPIO.output(dac, dec2bin(x))
                print("{:.2f}".format(3.3/256*x),' V')
finally:
    RPi.GPIO.output(dac, 0)
    RPi.GPIO.cleanup()
