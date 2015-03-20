import serial
import sys

#when function is run it should change the set point
#and recieve the new setpoint from arduino
ser = serial.Serial('/dev/ttyUSB2', 9600)
newsetpoint = 0
newsetpoint = sys.argv[1]


ser.write(newsetpoint)

#this will need some work in order to get the information from the arduino correctly
ser.read(Setpoint)
if newsetpoint = Setpoint:

   print('Setpoint set from argument')
else :
	print('error changing temp')