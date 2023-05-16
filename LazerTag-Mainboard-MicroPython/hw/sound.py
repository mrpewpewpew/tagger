import time
from machine import Pin, I2S
from micropython import schedule
import lib.sh1106 as sh1106

i2s = None
queue = []

# need an isr that calls schedule to send the next sound output
def __isr():
    pass

def __play():
    # TODO:
    # play sound from queue
    pass

def init(port:int, clock:int, wordclock:int, data:int, frequency:int) -> None:
    global i2s, sound

    i2s = I2S(
        port,
        sck=Pin(clock), 
        ws=Pin(wordclock), 
        sd=Pin(data),
        mode=I2S.TX,
        bits=16,
        format=I2S.MONO,
        rate=44100,
        ibuf=20000
    )

    load_samples()

class Sample(object):
    # TODO:
    pass

def load_samples():
    # TODO:
    # load samples off permanent storage into RAM ready to play them
    pass

def play(sound:Sample):
    queue.append(sound)
    schedule()