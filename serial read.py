# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:53:17 2015

@author: Steph

This script creates a serial port on windows machines "com" at the 
specified baud rate.  It will loop over a command sent to the port 
and print to a text file the full port response.  It also tracks
the time between writes.

"""

import datetime
import time
import serial

#Open Serial Port  -- update COM# and baud rate as needed
ser = serial.Serial('COM5', 115200)
start = time.time()

while ser.isOpen():

    try:

        f = open('your file name.txt', 'a') #Update output file name 
        ser.write("some text to serial port\r") #data to serial port
        info = ser.read(ser.inWaiting()) #read from serial port
        f.write('datetime: %s \n%s \n' % 
        (datetime.datetime.now(), info)) #write to text file
        print info
        time.sleep(10) #sleep until next write
        end = time.time()
        elapsed = end - start
        print elapsed


    except Exception, e:
        print "error: " + str(e)
        raise


