# https://docs.micropython.org/en/latest/library/machine.UART.html
from machine import Pin, UART, disable_irq, enable_irq
from micropython import schedule

import uasyncio

port:UART
latest:str = ""
received = []
r_count = 0

doReadFlag = uasyncio.ThreadSafeFlag()

def critical(func):
    def wrapper():
        x=disable_irq()
        func()
        enable_irq(x)
    return wrapper

async def ___recv_line() -> None:
    global port
    latest = port.readline()
    print("Received:" + str(latest))
    if latest != None:
        received.append(latest[:])

async def ___recv_task():
    while True:
        await doReadFlag.wait()
        uasyncio.create_task(___recv_line)

@critical
def __isr():
    global r_count
    r_count += 1
    doReadFlag.set()

def init(uart_port:int, tx_pin:int, rx_pin:int, baud:int) -> None:
    global port, latest_in, received
    rx_Pin = Pin(rx_pin)
    port = UART(uart_port, baudrate=baud, tx=Pin(tx_pin), rx=rx_Pin)
    port.init(baudrate=baud, bits=8, parity=None, stop=1)
    received = []
    uasyncio.create_task(___recv_task)
    rx_Pin.irq(
        __isr, 
        Pin.IRQ_FALLING, 
        hard=True
    )

def send(msg:str) -> bool:
    global port
    attempt = port.write(msg.encode("utf-8"))
    port.flush()

    if attempt == len(msg):
        return True
    else:
        return False