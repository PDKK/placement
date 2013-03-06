#!/usr/bin/python

from RpiLcdBackpack import AdafruitLcd
from colourSensor import ColourSensor
from Adafruit_PWM_Servo_Driver import PWM
from time import sleep
import smbus
import math

class Receiver:

  def __init__(self):
    self.bus=smbus.SMBus(0)
    self.pwm = PWM(0x40, debug=True, bus=self.bus)
    self.pwm.setPWMFreq(50)
    self.sensor=ColourSensor(self.bus)
    
    
  def setServoPulse(self, pulse):
    self.pwm.setPWM(0, 0, int(pulse * 4096 / 20))

  def readSensor(self):
    value=self.sensor.read()
    print "R%03X G%03X B%03X" % (value['red'], value['green'], value['blue'])
    if(value['blue'] <= 0x130) and (value['red'] <= 0x130): 
      return "Black" 
    elif(value['blue'] >= 0x155) and (value['red'] >= 0x155): 
      return "White"
    else:
      return "None"
      
  def dropMarble(self):
    self.setServoPulse(1.9)
    sleep(1)
    self.setServoPulse(1.6)	  
    sleep(1)
      
if __name__ == '__main__': 
  rx = Receiver()
  while True:
	value = rx.readSensor();
	if value == "None":
	  sleep(0.5)
	else:
	  print value
	  rx.dropMarble()
  
  
