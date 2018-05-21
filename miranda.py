# Miranda rover main control program
# USAGE is python miranda.py
# May 19, 2018 Version 1.0
# Steven Griset
# Engine control and basic object avoidance using sonar Coprocessor
# system randomly turns either clockwise or counter clockwise
# when an object is detected within 8 inches of the rover

# Load packages
import RPi.GPIO as GPIO     # import RPi.GPIO module
import sys                         # import sys for pathing
sys.path.append('/home/pi/zeroborg')    # path for zeroborg library
from time import sleep      # for a delay in the program
import ZeroBorg             # import motor controller library
from random import randint  # for random integer generation
# Setup GPIO
GPIO.setmode(GPIO.BCM)      # choose BCM Borad
GPIO.setup(17, GPIO.OUT, initial = 0)  # set GPIO17 as an output to power sonar circuit
GPIO.setup(23, GPIO.IN)  # set GPIO23 for input from sonar circuit
# Motor controller setup and GPIO pin initiation
# Setup ZeroBorg Motor
ZB = ZeroBorg.ZeroBorg()    # Create motor controller object
ZB.Init()                   # Setup the motor controller board
ZB.ResetEpo()               # Reset the safety latch
# ZB.SetCommsFailsafe(True)   # Set Failsafe to shutoff motors if Rpi and board loose connection
# Configure GPIO 18 to interrupt control flow when pin 18 goes high
GPIO.add_event_detect(23, GPIO.RISING)
# Set GPIO17 to 1/GPIO.HIGH/True to turn on circuit
GPIO.output(17, 1)
# ZB.GetCommsFailsafe()
# if a random number is even turn clockwise otherwise turn counterclockwise
def tangential_esc(x):
    if x % 2 == 0:
        clockwise()
        print "Turning Clockwise"
        sleep(0.20)
    else:
        counterclockwise()
        print "Turning Counterclockwise"
        sleep(0.20)


def clockwise():
    ZB.SetMotor1(-6)                    # Set motor 1 speed
    ZB.SetMotor2(.75)                     # Set motor 2 speed
    ZB.SetMotor3(.75)                     # Set motor 3 speed
    ZB.SetMotor4(-6)                    # Set motor 4 speed

def counterclockwise():
    ZB.SetMotor1(.75)                     # Set motor 1 speed
    ZB.SetMotor2(-6)                     # Set motor 2 speed
    ZB.SetMotor3(-6)                     # Set motor 3 speed
    ZB.SetMotor4(.75)                     # Set motor 4 speed

def main():
    print "Here we go! Press CTRL+C to exit"
    sleep(3.0)
    try:
        while True:
            print"Moving Forward"
            ZB.SetMotors(.65)

            if GPIO.event_detected(23):
                sleep(0.005)
                if(GPIO.input(23) == 1):
                    ZB.MotorsOff()
                    sleep(1.0)
                    x = randint(1, 100)  # generate a random number between 1 & 100
                    print "x equals %d" %x
                    tangential_esc(x)
                    ZB.MotorsOff()
                    print"Motors Off for 5 seconds"
                    sleep(5.0)
    except KeyboardInterrupt:    # Trap a CTRL+C keyboard interrupt
          ZB.MotorsOff()         # Turn off Motors
          GPIO.cleanup()         # Resets all GPIO ports used by this program

if __name__ == '__main__':
    main()
