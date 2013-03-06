#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
from time import sleep
import smbus
import math


class Transmitter:

  def __init__(self):
    self.bus=smbus.SMBus(1)
    self.pwm = PWM(0x40, debug=True, bus=self.bus)
    self.pwm.setPWMFreq(50)
    self.setServoPulse(1.5)

  def setServoPulse(self, pulse):
    self.pwm.setPWM(0, 0, int(pulse * 4096 /20))

  def send_left(self):
    self.setServoPulse(1.1)
    sleep(2)
    self.setServoPulse(1.5)
    sleep(2)

  def send_right(self):
    self.setServoPulse(1.8)
    sleep(2)
    self.setServoPulse(1.5)
    sleep(2)

if __name__ == '__main__':
  tx = Transmitter()
  tx.send_left()
  tx.send_left()
  tx.send_right()
  tx.send_right()

