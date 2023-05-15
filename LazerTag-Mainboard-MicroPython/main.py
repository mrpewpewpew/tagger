# /**
#     lazertag
#     Copyright (C) 2023 Benjamin Winston

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of 
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
#  */

# // hardware layout:
# //
# // i2c to CubeCell Heltec
# // i2c to display
# // i2c + DMA for music
# // pio via NEC library for IR transmission
# // pio via NEC library for IR reception (how many ports?)
# // UART for GPS

# // chip capability:
# //
# // fully-mux pins to any of the following or GPIO:
# //
# // - 2 x hardware UARTS
# // - 2 x hardware SPI
# // - 2 x hardware i2C
# // - 2 x Programmable IO modules, each capable of:
# //   -- 4 x state machines from the following prefabriated list,
# //          mapped to arbitrary pins:
# //   -- Any number of state machines can be adapted to be used
# //      for some custom protocol involving all 32 pins by writing
# //      some ridiculously simple assembly.
# //   -- Arbitrary mapping of pins, but also supporting mapping of
# //      multiple pins as a single input to a given state machine.
# //      This configuration is supported and allows us to provide 
# //      a logical OR of the input pins to the state machine input.
# //  

# // proposal:
# //
# // hardware i2c ports used for:
# //  - music
# //  - display
# //
# // hardware UART used for: 
# // - lorawan radio interface
# // - GPS
# //
# // leaving all eight state machines to be used for IR I/O
# //
# // nec_tx uses two state machines, 16 instructions and one IRQ
# // nec_rx uses one state machine and 9 instructions
# // 
# // I will modify the available NEC core to work with the higher
# // frequency demanded by the open source lazertag protocol

# globals

MODEM_TX            = 0 # gpio0 is pin 1
MODEM_RX            = 1 # gpio1 is pin 2
MODEM_PORT          = uart0 # uart hardware controller
MODEM_BAUD_RATE     = 115200

GPS_TX              = 4 # gpio4 is pin 6
GPS_RX              = 5 # gpio5 is pin 7
GPS_PORT            = uart1 # uart hardware controller
GPS_BAUD_RATE       = 115200

DISPLAY_DATA        = 6 # gpio6 is pin 9
DISPLAY_CLOCK       = 7 # gpio7 is pin 10
DISPLAY_PORT        = i2c1 # i2c hardware controller
DISPLAY_ADDRESS     = 0x3C
DISPLAY_BAUD_RATE   = 115200

SOUND_DATA          = 8 # gpio8 is pin 11
SOUND_CLOCK         = 9 # gpio9 is pin 12
SOUND_PORT          = i2c0 # i2c hardware controller

OPTIC_TX            = 10 # gpio10 is pin 14
OPTIC_RXS           = [ 11, 12, 13, 14, 15 ] # pins 15, 16, 17, 19, 20
OPTIC_PIO           = pio0 # programmable io controller

TRIGGER_RX          = 29
RECOIL_TX           = 27

# // core1 will handle:
# // optics, trigger pulls, recoil

# void main_core1() {
#     PIO pio = pio0;                                 // choose which PIO block to use (RP2040 has two: pio0 and pio1)
#     uint tx_gpio = 14;                              // choose which GPIO pin is connected to the IR LED
#     uint rx_gpio = 15;                              // choose which GPIO pin is connected to the IR detector

#     // configure and enable the state machines
#     int tx_sm = nec_tx_init(pio, tx_gpio);         // uses two state machines, 16 instructions and one IRQ
#     int rx_sm = nec_rx_init(pio, rx_gpio);         // uses one state machine and 9 instructions

#     // configure handlers
# }

# // core0 will handle:
# // modem comms, gps, gamestate, display and sound

# // UARTS: https://www.raspberrypi.com/documentation/pico-sdk/hardware.html#hardware_uart

def start_core0:
    
    pass


if __name__ == "__main__":
    start_core0()