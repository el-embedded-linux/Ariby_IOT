import RPi.GPIO as GPIO
import smbus
import math
import time

## Power management register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr) :
    return bus.read_byte_data(address, adr)

def read_word(adr) :
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr) :
    val = read_word(adr)

    if (val >= 0x8000):
        return -((65535 - val) + 1)

    else :
        return val


def dist(a,b) :
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z) :
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z) :
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)
    


bus = smbus.SMBus(1)
address = 0x68 ## My address value

## Power on MPU-6050
bus.write_byte_data(address, power_mgmt_1, 0)


try :
    while True:
        time.sleep(1)
        
        print ("----------------------------------")
        print ("=>Gyro data")
        print ("----------------------------------")


        gyro_xout = read_word_2c(0x43)
        gyro_yout = read_word_2c(0x45)
        gyro_zout = read_word_2c(0x47)


        print ("gyro_xout:{0:<15}".format(gyro_xout), "scaled:{0:<15}".format((gyro_xout / 131)))
        print ("gyro_yout:{0:<15}".format(gyro_yout), "scaled:{0:<15}".format((gyro_yout / 131)))
        print ("gyro_zout:{0:<15}".format(gyro_zout), "scaled:{0:<15}".format((gyro_zout / 131)))
        print ("\n")
        print ("----------------------------------")
        print ("=>Accelerometer data")
        print ("---------------------------------")


        accel_xout = read_word_2c(0x3b)
        accel_yout = read_word_2c(0x3d)
        accel_zout = read_word_2c(0x3f)

        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0


        print ("Accel_xout:{0:<15}".format(accel_xout), "scaled:{0:<15}".format(accel_xout_scaled))
        print ("Accel_yout:{0:<15}".format(accel_yout), "scaled:{0:<15}".format(accel_yout_scaled))
        print ("Accel_zout:{0:<15}".format(accel_zout), "scaled:{0:<15}".format(accel_zout_scaled))

        print ("x rotation:{0:<20}".format(get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)))
        print ("y rotation:{0:<20}".format(get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)))
        print ("--------------------------------")
        print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n") ## Screen Clear


except KeyboardInterrupt:
    GPIO.cleanup()


