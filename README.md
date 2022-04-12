# MCP4151
This library is for the MCP4151 digital potentiometer and its variants, although it is only tested on the MCP4151.<br>
It is designed to work on a Raspberry Pi and requires Python 3.


## Installation & Requirements
Just copy the library (MCP4151_lib.py) in your project folder.<br>
Requires "spidev" and "math". Normally preinstalled!

## Usage
Use MCP4151_0 if the device is connected to the Chipselect 0 (CE0) and the MCP4151_1 if it is connected to CE1.<br>
The values range from 0 to 255 (8-Bit)

## Extra
In the repo you will find the datasheet for the MCP413X/415X/423X/425X series and also the HydraSpex.lbr EagleLibrary that contains the MCP4151 for your Eagle project. There is also a connection example added to the repo.
