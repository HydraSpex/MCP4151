#!/usr/bin/env python

from MCP4151_0 import MCP4151_0
Poti = MCP4151_0()
Poti.write_pot(0)

while True:
    i = 0
    while i <= 255:
        print(i)
        Poti.write_pot(i) 
        i += 1