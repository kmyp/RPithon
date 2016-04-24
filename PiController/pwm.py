#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import re


def checknum(c):
    return bool(re.compile("^\d+\.?\d*\Z").match(c))


GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
#GPIO.output(16,True)

pin = GPIO.PWM(16,300)
dc =0
pin.start(dc)
while True:
    c = raw_input("input +/-:")

    if str.isdigit(c) or (c[:1] == "-" and str.isdigit(c[1:])):
        print c
        c = int(c)
        print c
        dc=dc+c
        
        if dc>100:
            dc=100
        if dc<0:
            dc=0
            
        pin.ChangeDutyCycle(dc)
        print dc

    if c=="exit":
        break


#GPIO.output(16,False)
pin.stop()

print "hello pi"

GPIO.cleanup()

