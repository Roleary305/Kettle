import serial
import sys

#when function is run it will read a 1 or 0 from arg and turn system on or off
#and recieve the new setpoint from arduino
ser = serial.Serial('/dev/ttyUSB2', 9600)
command = 0
command = sys.argv[1]

#arduino will read these as on or off

if command = 1:
	ser.write(666666)
	
if command = 0:
	ser.write(333333)
	