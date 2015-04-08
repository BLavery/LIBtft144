#   example-tft144.py          V1.6
#   Brian Lavery (C) Oct 2014    brian (at) blavery (dot) com
#   Free software.

# Demonstrates the "BLACK" or "RED" 128x128 SPI TFT board

# There are 3 variants of this file:
#      example-tft144.py
#      example-tft144-rpi-only.py
#      example-tft144-vgpio-only.py     <<<<<< THIS ONE



import virtGPIO as GPIO
from lib_tft144 import TFT144
from time import sleep
spidev = GPIO

RST =  8
CE =  10    # VirtGPIO: the chosen Chip Select pin#. (different meaning from rpi)
DC =   9
LED =  7
spidev = GPIO



# Don't forget the other 2 SPI pins SCK and MOSI (SDA)

TFT = TFT144(GPIO, spidev.SpiDev(), CE, DC, RST, LED, isRedBoard=False)


print ("Display character set:")
posx=0
posy=0
# Manual cursor moving
for i in range (32,256):
   TFT.put_char(chr(i),posx,posy,TFT.WHITE,TFT.BLACK)
   posx+=TFT.fontW
   if (posx+TFT.fontW)>128:
      posx=0
      posy+=TFT.fontH
sleep(2)


TFT.clear_display(TFT.BLUE)


print ("Message:")
# Automatic cursor moving
TFT.put_string("Hello,World!",28,28,TFT.WHITE,TFT.BLUE)  # std font 3 (default)
TFT.put_string("TFT144", 24,80,TFT.RED, TFT.BLUE, 4)     # doubled font 4
sleep(3)



print ("Rectangle")
TFT.draw_filled_rectangle(0,0,128,64 ,TFT.RED)
TFT.draw_filled_rectangle(0,64,128,128,TFT.BLACK)
for i in range (4,32,4):
   TFT.draw_rectangle(i,i,128-i,64-i,TFT.colour565(i-1,i-1,i-1))

print ("Line:")
TFT.draw_line(0,0,128,128,TFT.GREEN)
TFT.draw_line(0,128,128,0,TFT.GREEN)
