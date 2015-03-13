import time
import serial



ser = serial.Serial('/dev/ttyUSB2', 9600)



	
Setpoint = 93.00	

	


#Function to adjust set point.  Sends the 3 digit number which will corospond to a function on the arduino

def off():
    ser.write('sysoff')


def changeset(newsetpoint):

    ser.write(newsetpoint)
        

    if newsetpoint == Setpoint :
        print "Setpoint changed"
    
#Promt user for commands and the execute proper function
command = input("Enter Command")

if command == "temp":
    value = input('New Temp: ')
     
    changeset(str(value))

if command == "sleep" :
    ser.write(003)

