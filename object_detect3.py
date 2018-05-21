# March 25th 2018
# Testing miranda interrupt capabilities while in a control loop
# Using sonar circuit to detect object
# When Interrupt is called trun off motors for 3 seconds
# April 15th 2018
# Change to GPIO23 for pin interrupt
# Added new logic to prevent boucing of switch to dampen false detection 
import RPi.GPIO as GPIO     # import RPi.GPIO module
import sys                         # import sys for pathing
sys.path.append('/home/pi/zeroborg')    # path for zeroborg library
from time import sleep      # for a delay in the program
import ZeroBorg             # import motor controller library
GPIO.setmode(GPIO.BCM)      # choose BCM Borad
GPIO.setup(17, GPIO.OUT, initial = 0)  # set GPIO17 as an output to power sonar circuit
GPIO.setup(23, GPIO.IN)  # set GPIO23 for input from sonar circuit

# Setup ZeroBorg Motor
ZB = ZeroBorg.ZeroBorg()    # Create motor controller object
ZB.Init()                   # Setup the motor controller board
ZB.ResetEpo()               # Reset the safety latch

# Configure GPIO 18 to interrupt control flow when pin 23 goes high
GPIO.add_event_detect(23, GPIO.RISING)

GPIO.output(17, 1)  # set GPIO17 to 1/GPIO.HIGH/True to turn on circuit

print("Here we go! Press CTRL+C to exti")
sleep(2.0)
try:
    while True:
        ZB.SetMotors(.75)


        if GPIO.event_detected(23):
            sleep(0.005)
            if(GPIO.input(23) == 1):
                ZB.MotorsOff()
                print("You've been Interrupted")
                sleep(3.0)

except KeyboardInterrupt:   # trap a CTRL+C keyboard interrupt
    ZB.MotorsOff            # Turn off Motors
    GPIO.cleanup()         # Resets all GPIO ports used by this program

ZB.MotorsOff()             # Non-CTRL+C Motor Turn Off
GPIO.cleanup()             # Non-CTRL+C GPIO reset
