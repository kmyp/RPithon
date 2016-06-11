from __future__ import print_function
import socket
from contextlib import closing
import netifaces
import time
import re
import RPi.GPIO as GPIO
from RPIO import PWM

def main():
    host = netifaces.ifaddresses('wlan0')[netifaces.AF_INET][0]['addr']
    port = 10007
    bufsize = 128
    TIME = 60000
#     PWM.setup()
    GPIO.setmode(GPIO.BCM)
    

    pin_num = [5,6,13,19]
#     for i in range(0,4):
#         PWM.init_channel(i,15000)
#         
    for i in range(0,4):
#         PWM.add_channel_pulse(i,pin_num[i],0,100)
        GPIO.setup(pin_num[i], GPIO.OUT)
#     GPIO.setup(21,GPIO.OUT)
#     pwmpin= GPIO.PWM(21,500)
#     pwmpin.start(50)
    pin = [GPIO.PWM(5,50),GPIO.PWM(6,50),GPIO.PWM(13,50),GPIO.PWM(19,50)]
    
    for i in range(0,4):
        pin[i].start(7.5)
        
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    with closing(sock):
        sock.bind((host, port))
        while True:
            cmd = sock.recv(bufsize)
            if cmd=="stop":
                print("stop")
                for i in range(0,4):
                    pin[i].stop()       
#                 pwmpin.stop()             
                return

            cmd = cmd.split(",")       
            print(cmd)     
            
            for i in range(0,4):
#                 PWM.clear_channel(i)
#                 pin[i].ChangeFrequency(int(1.0/float(cmd[i*2+1])*1000000)+100)
                pin[i].ChangeDutyCycle(float(float(cmd[i*2+1])/200))
                print(float(float(cmd[i*2+1])/200))
#                 PWM.add_channel_pulse(i,pin_num[i],0,int(cmd[i*2+1])/10)
            
    return

    
if __name__ == '__main__':
  main()
  PWM.cleanup()
  GPIO.cleanup()
