#!/usr/bin/env python

import spidev
import math

class MCP4151_0(object):
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 976000                          #Set to preferred Speed

    def write_pot(self, input):                                 #Input can be 0-255
        msb = input >> 8
        lsb = input & 0xFF
        self.spi.xfer([msb, lsb])
