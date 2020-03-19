
import serial

with serial.Serial('/dev/ttyACM0',115200) as ser:  # open serial port
    #print(ser.name)
    buffer = []
    print("read from UART at: ".format(ser.name))
    while True:
        #print("read from serial")
        if ser.is_open:
            next = ser.read()
            if next == '?':
                print(buffer)
                buffer=[]
            else:
                buffer.append(next)
                #print(buffer)
        else:
            break
