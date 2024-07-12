import serial
import serial.tools.list_ports
import time

def start_treadmill():
    # Get a list of all available ports
    available_ports = list(serial.tools.list_ports.comports())

    if not available_ports:
        print("No COM ports found.")
    else:
        print("Available COM ports:")
        for port in available_ports:
            print(port.device)

    ser = serial.Serial('COM3', 9600)
    ser.close()
    ser.parity = serial.PARITY_NONE  # Set parity to none
    ser.stopbits = serial.STOPBITS_ONE
    ser.bytesize =  serial.EIGHTBITS
    ser.timeout = 1  # Set a timeout of 1 second
    ser.open()

    turn_on = [0xAE, 0x30, 0x30, 0x0D, 0xA2, 0x30, 0x30, 0x0D, 0xA6, 0x31, 0x0d, 0xA5, 0x0D]
    start = [0xA9,0x0D]
    set_direction_forward = [0xB8, 0x30, 0x0D]
    set_speed = [0xA3, 0x30, 0x31, 0x35, 0x30, 0x0D]
    set_direction_reverse = [0xB8, 0x31, 0x0D]
    stop = [0xA8 , 0x0D]

    byte_list = bytes(turn_on)
    ser.write(byte_list)
    time.sleep(10)
    
    byte_list = bytes(start)
    ser.write(byte_list)
    time.sleep(1)
        

    for i in range (3):
            
        byte_list = bytes(set_direction_forward)
        ser.write(byte_list)
        time.sleep(2)

        byte_list = bytes(set_speed)
        ser.write(byte_list)
        time.sleep(6)
        
        byte_list = bytes(set_direction_reverse)
        ser.write(byte_list)
        time.sleep(2)

        byte_list = bytes(set_speed)
        ser.write(byte_list)
        time.sleep(6)

    byte_list = bytes(stop)
    ser.write(byte_list)
    time.sleep(1)

    time.sleep(5)
    ser.close()
