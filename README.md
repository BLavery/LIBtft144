# lib_tft144

## May 2018 - This is no longer being maintained by the original author.
## Please feel free to fork, copy, adapt if you find it useable

V1.6    April 2015

LCD-TFT-1.44 128x128px.  An SPI library for Raspberry Pi or Virtual GPIO.

The "BLACK" 1.44 board from eBay -    eg http://www.ebay.com.au/itm/141239781210     - under $4!

The "RED" version. eg. http://www.ebay.com.au/itm/400685907981

RED board has a hardware mistake that preconfigures to 128x160 instead of 128x128.
V1.6 of this library corrects for the red board error, but YOU MUST SET "isRedBoard=True" in the TFT144 object constructor.
Otherwise some display modes have screen contents jumbled.

Board has inbuilt 5V-3V (2.9?) regulator (which does NOT break out the 3V!!)
As far as I can discern, logic level is still 3.3V limit, despite supply is 5V.
Currently the code here is designed simply for case of 128x128 pixels.
Brian Lavery (C) Oct 2014    brian (at) blavery (dot) com
Free software, derived from:
   (1) ILI9163 128x128 LCD library   - parallel I/O AVR C code
      Copyright (C) 2012 Simon Inns
      http://www.waitingforfriday.com/index.php/Reverse_Engineering_a_1.5_inch_Photoframe
   (2) ... then Antares python/parallel Raspberry Pi code:
      http://www.raspberrypi.org/forums/viewtopic.php?t=58291&p=450201

Added: SPI access, BMP file load, double size fonts, python class, python3/2.7 compatibility
Works on: Rasp Pi GPIO,    or "virtual GPIO" 3.3V   (identical library for both)

On Raspberry Pi, uses SpiDev and RPi.GPIO.


                   THIS BOARD WORKS A TREAT !!!!



See examples files  for Raspberry Pi use, virtual-GPIO use, and "smart" GPIO selection (RPi or virtual)
