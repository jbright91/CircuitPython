import time
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import servo
import pwmio

btn = DigitalInOut(board.D4)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

pwm = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)
angle = 180


btn2 = DigitalInOut(board.D6)
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP

while True:
    if not btn.value:
        print("BTN is down")
        for angle in range(0, 180, 9):  # 0 - 180 degrees, 5 degrees at a time
            my_servo.angle = angle 
            time.sleep(0.1)
    else:
        print("BTN is up")
        pass
    if not btn2.value:
        print("BTN2 is down")
        for angle in range(180,0, -9):  # 0 - 180 degrees, -5 degrees at a time
            my_servo.angle = angle 
            time.sleep(0.1)
    else:
        print("BTN2 is up")
        pass

    time.sleep(0.1) # sleep for debounce