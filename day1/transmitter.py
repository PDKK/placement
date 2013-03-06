#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
from time import sleep
import smbus
import math

def setServoPulse(pulse):
  pwm.setPWM(0, 0, int(pulse * 4096 /20))



if __name__ == '__main__':
  bus=smbus.SMBus(1)
  pwm = PWM(0x40, debug=True, bus=bus)
  pwm.setPWMFreq(50)
  while True:
    pulse = input("What position would you like the servo at: " )
    setServoPulse(pulse)




