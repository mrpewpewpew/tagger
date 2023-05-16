import time
from machine import Pin, I2C
import lib.sh1106 as sh1106

i2c = None
display = None

def init(port:int, clock:int, data:int, frequency:int, address:int):
    global i2c, display
    i2c = I2C(port, scl=Pin(clock), sda=Pin(data), freq=freq)
    display = sh1106.SH1106_I2C(128, 64, i2c, Pin(2), address)
    display.sleep(False)
    display.fill(0)
    display.rotate(1)
    display.text('Testing X', 0, 0, 1)
    display.show()
