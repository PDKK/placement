#!/usr/bin/python
import time
from RpiLcdBackpack import AdafruitLcd 

if __name__=='__main__':
    display = AdafruitLcd()
    display.backlight(True)
    time.sleep(5)
    display.message("Hello LCD.\nThis is Rowan.")
    time.sleep(5)
    display.clear()
    time.sleep(5)
    display.backlight(False)
