#   example-tft144.py          V1.6
#   Brian Lavery (C) Oct 2014    brian (at) blavery (dot) com
#   Free software.

# Demonstrates the "BLACK" & "RED" 128x128 SPI TFT board

# There are 3 variants of this file:
#      example-tft144.py                <<<< THIS ONE  - picks virtual or raspberry automatically
#      example-tft144-rpi-only.py
#      example-tft144-vgpio-only.py



from smartGPIO import GPIO
from lib_tft144 import TFT144
from time import sleep


# My tests. Two configurations.

if GPIO.RPI_REVISION == 0:   # VIRTUAL-GPIO
    RST =  8
    CE =  10    # VirtGPIO: the chosen Chip Select pin#. (different from rpi)
    DC =   9
    LED =  7
    spidev = GPIO
    # the virtual GPIO module directly supports spidev function

else:   # RPI
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    RST = 18    # RST may use direct +3V strapping, and then be listed as 0 here. (Soft Reset used instead)
    CE =   0    # RPI GPIO: 0 or 1 for CE0 / CE1 number (NOT the pin#)
    DC =  22    # Labeled on board as "A0"   Command/Data select
    LED = 23    # LED may also be strapped direct to +3V, (and then LED=0 here). LED sinks 10-14 mA @ 3V
    import spidev



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
