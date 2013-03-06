#

import smbus, time



class ColourSensor:
  __ADDRESS=0x74

  __CONTROL=0x0

  __CAP_RED=0x6
  __CAP_GREEN=0x7
  __CAP_BLUE=0x8
  __CAP_CLEAR=0x9

  __INT_RED=0xA
  __INT_GREEN=0xC
  __INT_BLUE=0xE
  __INT_CLEAR=0x10
  
  __DATA_RED=0x40
  __DATA_GREEN=0x42
  __DATA_BLUE=0x44
  __DATA_CLEAR=0x46

  def __init__(self, bus=None):
    if bus == None:
      self.__bus = smbus.SMBus(0)
    else:
      self.__bus = bus
    self.setCapacitors(2,2,2,2)
    self.setIntegrators(0x100,0x100,0x100,0x100)

  def setCapacitors(self, red, green, blue, clear):
    self.__bus.write_byte_data(self.__ADDRESS,self.__CAP_RED,red)
    self.__bus.write_byte_data(self.__ADDRESS,self.__CAP_GREEN,green)
    self.__bus.write_byte_data(self.__ADDRESS,self.__CAP_BLUE,blue)
    self.__bus.write_byte_data(self.__ADDRESS,self.__CAP_CLEAR,clear)

  def setIntegrators(self, red, green, blue, clear):
    self.__bus.write_word_data(self.__ADDRESS,self.__INT_RED,red)
    self.__bus.write_word_data(self.__ADDRESS,self.__INT_GREEN,green)
    self.__bus.write_word_data(self.__ADDRESS,self.__INT_BLUE,blue)
    self.__bus.write_word_data(self.__ADDRESS,self.__INT_CLEAR,clear)

  def read(self):
    self.__bus.write_byte_data(self.__ADDRESS, self.__CONTROL, 0x1)
    while self.__bus.read_byte_data(self.__ADDRESS,self.__CONTROL) == 1:
      time.sleep(0.1)
    result = {}
    result['red'] = self.__bus.read_word_data(self.__ADDRESS,self.__DATA_RED)
    result['blue'] = self.__bus.read_word_data(self.__ADDRESS,self.__DATA_GREEN)
    result['green'] = self.__bus.read_word_data(self.__ADDRESS,self.__DATA_BLUE)
    result['clear'] = self.__bus.read_word_data(self.__ADDRESS,self.__DATA_CLEAR)
    return result


if __name__ == "__main__":
  bus=smbus.SMBus(0)
  sensor=ColourSensor(bus)

  while True:
    print sensor.read()



