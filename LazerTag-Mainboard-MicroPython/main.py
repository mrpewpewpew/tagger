import time
from machine import Pin, I2C
import lib.sh1106 as sh1106

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(2), 0x3c)
display.sleep(False)
display.fill(0)
display.rotate(1)
display.text('Testing 1', 0, 0, 1)
display.show()
