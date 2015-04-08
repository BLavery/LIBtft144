#!/usr/bin/python
# -*- coding: utf-8 -*-

# AUTO: Find if operating on Raspberry Pi GPIO system or on virtual GPIO on PC

if __name__ == '__main__':
    import sys
    print ('%s is an importable module:' % sys.argv[0])
    print ("...  from smartGPIO import GPIO")
    print ("")
    exit()


try:
    # This para is the vGPIO attempt:
    import virtGPIO as GPIO
    # That succeeded

except:
    try:
        # This para is the RPI-GPIO attempt:
        import RPi.GPIO as GPIO
        # That succeeded


    except:
        print ("No GPIO?")
        exit()
