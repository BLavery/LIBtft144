
# example-tft144-fonts.py     V1.1

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

else:   # RPI
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    RST = 18    # RST may use direct +3V strapping, and then be listed as 0 here. (Soft Reset used instead)
    CE =   0    # RPI GPIO: 0 or 1 for CE0 / CE1 number (NOT the pin#)
    DC =  22    # Labeled on board as "A0"   Command/Data select
    LED = 23    # LED may also be strapped direct to +3V, (and then LED=0 here). LED sinks 10-14 mA @ 3V
    import spidev



#  Don't forget the other 2 SPI pins SCK and MOSI (SDA)

#  OK, GPIO (of one variety) is all ready. Now do the LCD demo:


TFT = TFT144(GPIO, spidev.SpiDev(), CE, DC, RST, LED, TFT144.ORIENTATION90)
# TFT = TFT144(GPIO, spidev.SpiDev(), CE, DC)     # the minimalist version


TFT.clear_display(TFT.BLUE)
sleep(1)
TFT.clear_display(TFT.RED)
sleep(1)
TFT.clear_display(TFT.GREEN)
sleep(1)
TFT.clear_display(TFT.PINK)
sleep(1)
TFT.clear_display(TFT.LIGHTBLUE)
sleep(1)
TFT.clear_display(TFT.LIGHTGREEN)
sleep(1)
TFT.clear_display(TFT.YELLOW)
sleep(1)
TFT.clear_display(TFT.MAGENTA)
sleep(1)
TFT.clear_display(TFT.CYAN)
sleep(1)

TFT.clear_display(0)

print ("Display character sets:")
for f in range(1, 9):
    posx=0
    posy=0
    print ("Font %d" % f) ,
    print ("Base Font" if (f%2) else "Doubled Font"),
    print ("(default)" if f==3 else "")
    for i in range (33,126):
       #  Note manual handling of cursor here (character output)
       TFT.put_char(chr(i),posx,posy,TFT.WHITE,TFT.BLACK,f)
       posx+=TFT.fontW
       if (posx+TFT.fontW)>=127:
          posx=0
          posy+=TFT.fontH
       if (posy+TFT.fontH)>=128:
           break

    sleep(1)
    TFT.clear_display(0)

print ("Extended char set for fonts 3,4")
posx=0
posy=0
for i in range (1,256):
   #  Note manual handling of cursor here (character output)
   TFT.put_char(chr(i),posx,posy,TFT.WHITE,TFT.BLACK)
   posx+=TFT.fontW
   if (posx+TFT.fontW)>=127:
      posx=0
      posy+=TFT.fontH
   if (posy+TFT.fontH)>=128:
       break

sleep(4)
TFT.clear_display(0)


print ("String output: 4 base fonts")
# Note here the character positioning, wrap etc is auto
TFT.put_string("Quick Brown fox jumped over", 0,0,TFT.WHITE, TFT.BLACK,1)
TFT.put_string("Quick Brown fox jumped over", 0,20,TFT.LIGHTBLUE, TFT.BLACK,3)
TFT.put_string("Quick Brown fox jumped over", 0,55,TFT.LIGHTGREEN, TFT.BLACK,5)
TFT.put_string("Quick Brown fox jumped over", 0,90,TFT.PINK, TFT.BLACK,7)

sleep(6)
TFT.clear_display(TFT.BLUE)
TFT.put_string("Fin.", 30, 40, TFT.WHITE, TFT.BLUE, 8)
