from machine import Pin     # loads the GPIO Pin library from the machine module
import time                 # loads the time module

led = Pin('D4', Pin.OUT)    # defines "led" as an output on pin D4

while True:                 # run this section of code forever
    led.on()                # turn on the LED
    print('LED on')      # show LED state in the terminal
    time.sleep(1)           # wait for one second
    led.off()               # turn off the LED
    print('LED off')     # show LED state in the terminal
    time.sleep(1)           # wait for one second
