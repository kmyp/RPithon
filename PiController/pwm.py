#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import re


def checknum(c):
    return bool(re.compile("^\d+\.?\d*\Z").match(c))


GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

pin = GPIO.PWM(16,1500)
dc =50
freq = 1500
pin.start(dc)
while True:
    c = raw_input("input +/-:")

    if str.isdigit(c) or (c[:1] == "-" and str.isdigit(c[1:])):
        print c
        c = int(c)
        print c
        freq=freq+c

        if freq>2000:
            freq=2000
        if freq<1000:
            freq=1000

        pin.ChangeFrequency(freq)
        print freq

    if c=="exit":
        break


pin.stop()


GPIO.cleanup()

