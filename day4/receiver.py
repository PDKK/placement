#!/usr/bin/python

from RpiLcdBackpack import AdafruitLcd
from colourSensor import ColourSensor
from Adafruit_PWM_Servo_Driver import PWM
from time import sleep
import smbus
import math
from morseParity import MorseParity
import sys

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
    if(value['blue'] <= self.blackBlue ) and (value['red'] <= self.blackRed): 
      return "-" 
    elif(value['blue'] >= self.whiteBlue) and (value['red'] >= self.whiteRed): 
      return "."
    else:
      return "None"
      
  def dropMarble(self):
    self.setServoPulse(1.9)
    sleep(1)
    self.setServoPulse(1.6)   
    sleep(1)

  def calibrateBlack(self):
    self.blackValue = {'red':0, 'green':0, 'blue':0 }
    for i in range(10):
      value=self.sensor.read()
      self.blackValue['red'] += value['red']
      self.blackValue['blue'] += value['blue']
      self.blackValue['green'] += value['green']
      sleep(0.2)
    self.blackValue['red'] /= 10
    self.blackValue['green'] /= 10
    self.blackValue['blue'] /= 10
      
  def calibrateWhite(self):
    self.whiteValue = {'red':0, 'green':0, 'blue':0 }
    for i in range(10):
      value=self.sensor.read()
      self.whiteValue['red'] += value['red']
      self.whiteValue['blue'] += value['blue']
      self.whiteValue['green'] += value['green']
      sleep(0.2)
    self.whiteValue['red'] /= 10
    self.whiteValue['green'] /= 10
    self.whiteValue['blue'] /= 10

  def calibrateNone(self):
    self.noneValue = {'red':0, 'green':0, 'blue':0 }
    for i in range(10):
      value=self.sensor.read()
      self.noneValue['red'] += value['red']
      self.noneValue['blue'] += value['blue']
      self.noneValue['green'] += value['green']
      sleep(0.2)
    self.noneValue['red'] /= 10
    self.noneValue['green'] /= 10
    self.noneValue['blue'] /= 10
    self.blackRed = (self.blackValue['red'] + self.noneValue['red'])/2
    self.blackBlue = (self.blackValue['blue'] + self.noneValue['blue'])/2
    self.whiteRed = (self.whiteValue['red'] + self.noneValue['red'])/2
    self.whiteBlue = (self.whiteValue['blue'] + self.noneValue['blue'])/2
      
if __name__ == '__main__': 
  rx = Receiver()
  display = AdafruitLcd()
  codec = MorseParity()
  currentReceived = ""
  message = ""
  timeout = 0

  display.clear()
  display.message("Calibrating Black")
  sleep(5)
  rx.calibrateBlack()
  rx.dropMarble()

  display.clear()
  display.message("Calibrating White")
  sleep(5)
  rx.calibrateWhite()
  rx.dropMarble()

  display.clear()
  display.message("Calibrating None")
  rx.calibrateNone()
  
  
  
  while True:
    value = rx.readSensor();
    if value == "None":
      sleep(0.5)
      timeout = timeout + 0.5
      
      if timeout >= 5.9 and timeout <= 6.1:
          message = message + " "
          display.clear()
          display.message((message) + "\n" +(currentReceived))
          display.message(" ")
          display.backlight(False)
    else:
      currentReceived = currentReceived + value
      rx.dropMarble()
      timeout = 0
      display.backlight(True)
      display.message("\n" + currentReceived)
      while timeout < 3:
        value = rx.readSensor();
        if value == "None":
            sleep(0.5)
            timeout = timeout + 0.5
        else:
            currentReceived = currentReceived + value
            rx.dropMarble()
            timeout = 0
            display.message(currentReceived)
      message = message + codec.decode(currentReceived)
      display.clear()
      display.message((message) + "\n" +(currentReceived))
      currentReceived = ""
