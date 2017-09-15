import serial
import time
import pprint
port = "COM6"
baud = 9600

ser = serial.Serial(port, baud, timeout=1)
# open the serial port
if ser.isOpen():
    print(ser.name + ' is open...')

while 1:
    try:
        print(ser.readline())
        time.sleep(1/baud)
    except ser.SerialTimeoutException:
        print('Data could not be read')
        time.sleep(1)
