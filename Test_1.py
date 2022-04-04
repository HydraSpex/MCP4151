#!/usr/bin/env python

from MCP4151_lib import MCP4151_1                   #Import MCP4151_0 for connection on CE0 and MCP4151_1 for connection on CE1
Poti = MCP4151_1()
Poti.write_pot(0)                                 #Input can be 0-255

while True:
    i = 0
    while i <= 255:
        print(i)
        Poti.write_pot(i) 
        i += 1
