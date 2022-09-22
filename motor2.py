import time
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import servo
import pwmio

pwm = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)
btn = DigitalInOut(board.D4)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
my_servo = servo.Servo(pwm)
angle = 180

pwm = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)
btn = DigitalInOut(board.D4)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
my_servo = servo.Servo(pwm)
angle = 180

while True:
    if not btn.value:
        print("BTN is down")
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time
            my_servo.angle = angle 
            time.sleep(0.1)
    else:
        print("BTN is up")
        pass

    time.sleep(0.1) # sleep for debounce
