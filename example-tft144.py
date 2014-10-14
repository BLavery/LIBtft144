#   example-tft144.py          V1.0
#   Brian Lavery (C) Oct 2014    brian (at) blavery (dot) com
#   Free software.

# Demonstrates the "BLACK" 128x128 SPI TFT board connected to regular Raspberry Pi

from LIBtft144 import TFT144
from time import sleep

# Do NOT have files virtGPIO.py & vGPIOconstants.py on the RPI. That would trigger an attempt to use virt GPIO.


# My BCM GPIO numbers
RST = 18
CE =   0    # 0 or 1 for CE0 / CE1 number (NOT the pin#)
DC =  22    # Labeled on board as "A0"
LED = 23    # LED backlight sinks 10-14 mA @ 3V


TFT = TFT144(CE, DC, RST, LED)


posx=0
posy=0
print "Display character set:"
for i in range (32,256):
   TFT.put_char(chr(i),posx,posy,TFT.WHITE,TFT.BLACK)
   posx+=6
   if posx>=121:
      posx=0
      posy+=8
sleep(2)


TFT.clear_display(TFT.BLUE)


print "Message:"
TFT.put_string("Hello,World!",28,28,TFT.WHITE,TFT.BLUE)  # small font (size = 1 default)
TFT.put_string("TFT144", 24,80,TFT.RED, TFT.BLUE, 2)     # large font (size = 2)
sleep(3)



print "Rectangle"
TFT.draw_filled_rectangle(0,0,128,64 ,TFT.RED)
TFT.draw_filled_rectangle(0,64,128,128,TFT.BLACK)
for i in range (4,32,4):
   TFT.draw_rectangle(i,i,128-i,64-i,TFT.rgb(i-1,i-1,i-1))

print "Line:"
TFT.draw_line(0,0,128,128,TFT.GREEN)
TFT.draw_line(0,128,128,0,TFT.GREEN)
