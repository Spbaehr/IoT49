from machine import PWM, Pin
from board import *
import time

# declare pins
pin1 = Pin(A18, mode=Pin.OUT)
pin2 = Pin(A19, mode=Pin.OUT)

# initialize PWM
pwm1 = PWM(pin1, freq=1000)
pwm2 = PWM(pin2, freq=1000)

# set duty cycle (0 ... 1023)
pwm1.duty(300)
pwm2.duty(700)

# go about other business (or just take a nap)
time.sleep(10000)

# release PWM circuitry for later reuse
pwm1.deinit()
pwm2.deinit()
