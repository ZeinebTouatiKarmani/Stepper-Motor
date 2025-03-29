# control step motor with  Stepper Motor Driver A4988
from machine import Pin
import time

dir=Pin(1, Pin.OUT)
step=Pin(2, Pin.OUT)

dir.value(1)
for n in range (200):
    step.value(0)
    time.sleep(0.01)
    step.value(1)
    time.sleep(0.01)

dir.value(0)
for n in range (100):
    step.value(0)
    time.sleep(0.01)
    step.value(1)
    time.sleep(0.01)