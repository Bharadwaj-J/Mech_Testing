import serial
import serial.tools.list_ports
import time

def start_treadmill(speed,inc):
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
    
    # Calculating speed
    speed_int = int(speed)
    speed_dec = int(speed*100)%100
    speed_dec_1 = (speed_dec//10)%10
    speed_dec_2 = speed_dec%10
    set_speed = [0xA3, 0x30+speed_int, 0x30+speed_dec_1, 0x30+speed_dec_2, 0x30, 0x0D]

    #Inclination Calculation
    inc_int = int(inc)
    inc_dec = int(inc*100)%100
    inc_dec_1 = (inc_dec//10)%10
    set_inc = [0xA4, 0x30, 0x30, 0x30+inc_int, 0x30+inc_dec_1, 0x0D]
    
    byte_list = bytes(turn_on)
    ser.write(byte_list)
    time.sleep(10)
    
    byte_list = bytes(start)
    ser.write(byte_list)
    time.sleep(1)

    byte_list = bytes(set_direction_forward)
    ser.write(byte_list)
    time.sleep(2)
    
    byte_list = bytes(set_inc)
    ser.write(byte_list)
    time.sleep(6)

    byte_list = bytes(set_speed)
    ser.write(byte_list)

    time.sleep(2)
    ser.close()

def stop_treadmill():
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

    stop = [0xA2, 0x30, 0x30, 0x0D, 0xA6, 0x30, 0x0D]

    byte_list = bytes(stop)
    ser.write(byte_list)

    time.sleep(10)
    ser.close()