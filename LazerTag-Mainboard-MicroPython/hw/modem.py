# https://docs.micropython.org/en/latest/library/machine.UART.html

from machine import Pin, UART, disable_irq, enable_irq
from micropython import schedule

port = None
latest = ""
received = []
r_count = 0

def critical(func):
    def wrapper():
        disable_irq()
        func()
        enable_irq()
    return wrapper

@critical
def __recv():
    latest = port.readline()
    received.append(latest[:])

@critical
def __isr():
    r_count+=1
    schedule(recv)

def init(uart_port:int, tx_pin:int, rx_pin:int, baud:int) -> None:
    global port, latest_in, received
    port = UART(uart_port, baudrate=baud, tx=Pin(tx_pin), rx=Pin(rx_pin))
    port.init(baudrate=baud, bits=8, parity=None, stop=1)
    received = []
    port.irq(UART.rx_any, priority=1, handler=__isr)

def send(msg:str) -> bool:
    global port
    attempt = port.write(msg)
    port.flush()

    if attempt == len(msg):
        return True
    else:
        return False