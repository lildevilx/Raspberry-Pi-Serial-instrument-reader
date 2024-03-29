#!/usr/bin/env python3

#Insert description....

#to add
#-The use of wait time
#-option for poll/broadcast data
#-option for reading end of string

from datetime import datetime
import time
import serial

#####################
######Variables######
#####################

FN = "%Y%m%d-Intermet" #Name you want the file to be called with
FL = "/home/pi/data/" #Location you want the to save the data at
TSF = "%H:%M:%S," #Time stamp format
ser_port = "/dev/ttyUSB0" #name of serial port
ser_baud = "57600" #serial baud rate
waittime = 0.5 #seconds to wait in between reads (Not used)

#####################
########Setup########
#####################
data1=" "
#####################
########Main#########
#####################
sercheck = True
while sercheck == True:
  try: 
    ser = serial.Serial(ser_port, ser_baud)
    ser.close()
    print("Found, starting to log")
    sercheck = False
  except serial.serialutil.SerialException:
    print(ser_port+' not find, retry in 3 seconds\n')
    time.sleep(3)
while True:
  try:
    now = datetime.now()
    FM= now.strftime(FN)
    NF=open(FL+FM+'.csv','a') #setup file name to save
    ser = serial.Serial(ser_port, ser_baud) #open serial port
    data = ser.read_until(b'\r\n') #read serial data
    #print(data)
    now = datetime.now()
    TS = now.strftime(TSF)
    if data1 != data:
      #print("saveing data " +TS+str(data)[8:][:-5])
      NF.write(TS+str(data)[8:][:-5]+'\r\n')
      data1 = data
    ser.close()
    NF.close()
  except: 
    ser.close()
    NF.close()
    exit()
