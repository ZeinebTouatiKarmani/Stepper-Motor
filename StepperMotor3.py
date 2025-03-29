# control step motor with  Stepper Motor Driver A4988
from machine import Pin
import time

class StepperMotor:
    def __init__(self, dir_pin, step_pin, pulse_width_ms=10, steps_per_revolution=800):
        self.dir = Pin(dir_pin, Pin.OUT)
        self.step = Pin(step_pin, Pin.OUT)
        self.pulse_width_ms = pulse_width_ms
        self.steps_per_revolution = steps_per_revolution
        self.current_position_steps = 0
        self.current_position_degrees = 0
        
    def degrees_to_steps(self, degrees):
        """Convert degrees to number of steps needed"""
        return int((degrees * self.steps_per_revolution) / 360)
    
    def steps_to_degrees(self, steps):
        """Convert steps to degrees"""
        #return (steps * 360) / self.steps_per_revolution
        return ((steps%800) * 360) / self.steps_per_revolution
    
    def rotate_steps(self, num_steps):
        """Rotate motor by specified number of steps, handling direction"""
        direction = 1 if num_steps > 0 else 0  # Set direction (CW = 1, CCW = 0)
        self.dir.value(direction)  # Set the direction pin **before stepping**
        for i in range(abs(num_steps)):
            #self.step.toggle()
            #time.sleep_ms(self.pulse_width_ms)
            self.step.value(1)  # HIGH
            time.sleep_us(1000)  # 1 ms pulse width (adjust if needed)
            self.step.value(0)  # LOW
            time.sleep_us(1000)  # Allow motor to respond
                
            
        # Update position
        self.current_position_steps += num_steps
        self.current_position_degrees = self.steps_to_degrees(self.current_position_steps)
        
    def rotate_degrees(self, degrees):
        """Rotate motor by specified angle in degrees"""
        steps_needed = self.degrees_to_steps(degrees)
        self.rotate_steps(steps_needed)
        
        
    def get_position(self):
        """Return current position in degrees"""
        return self.current_position_degrees
        
    def reset_position(self):
        """Reset position counters to zero"""
        self.current_position_steps = 0
        self.current_position_degrees = 0

# Usage example
motor = StepperMotor(1, 2)

# Rotate 360 degrees clockwise
motor.rotate_steps(-700)
print(f"Position1 controlled by steps  : {motor.get_position()}°")
time.sleep(2)

# Rotate 360 degrees counterclockwise
motor.rotate_degrees(180)
print(f"Position2 controlled by degree: {motor.get_position()}°")
time.sleep(2)

print("Position3: controlled by the user: ")
angle = int(input("Enter angle to rotate: "))  # Convert input to integer
motor.rotate_degrees(angle)
print(f"Position3: {motor.get_position()}°")
time.sleep(2)

# Reset to zero position
motor.reset_position()