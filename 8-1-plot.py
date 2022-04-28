import numpy
import matplotlib.pyplot as plt
import os

try:
    os.chdir(r"/home/b04-107/Desktop/Scripts/7-1-files")
    f1 = open("data.txt")
    f2 = open("settings.txt")
    freq, step = f2.read().split('\n')
    freq = float(freq)
    step = float(step)
    y = numpy.array(list(map(int, f1.read().split('\n'))))
    y = y * 3.3 / 256
    x = numpy.arange(0, numpy.size(y) * step, step)
    fig, ax = plt.subplots(figsize = (16, 8), dpi = 400)
    ax.set_ylabel("Voltage, V")
    ax.set_xlabel("Time, s")
    ax.set_title("Charging-discharging process (RC-chain)")
    plt.plot(x, y, lw = 2, ms = 12, c = 'yellow', marker = '*', mfc = 'red', ls = '-', markevery = 50, drawstyle = 'default', label = 'V(t)')
    ax.minorticks_on()
    plt.grid(which = 'major', color = 'green', ls = '--', lw = 1)
    plt.grid(which = 'minor', color = 'grey', ls = '--', lw = 0.5)
    plt.text(60, 2.4, 'Charging time = '+str(round(numpy.argmax(y)*step, 2))+' s', color = 'purple')
    plt.text(60, 2.2, 'Discharging time = '+str(round((numpy.size(y) - numpy.argmax(y))*step, 2))+' s', color = 'purple')
    plt.legend()
    plt.savefig("plot.png")
    plt.show()
finally:
    f1.close()
    f2.close()