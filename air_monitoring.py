import time
import serial
#testcomment


ser = serial.Serial('/dev/serial0', 9600, timeout=1)

while True:
    result=ser.write(b"\xff\x01\x86\x00\x00\x00\x00\x00\x79")
    s=ser.read(9)
    if s[0] == 0xff and s[1] == 0x86:
        print ("CO2 = " + str(s[2]*256 + s[3]))
    time.sleep(1)
