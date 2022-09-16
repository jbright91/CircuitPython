import board
import time
import pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.D5, duty_cycle=0, frequency=250)

servo = servo.Servo(pwm)

# We sleep in the loops to give the servo time to move into position.
print("Sweep from 0 to 180")
for i in range(180):
    servo.angle = i
    time.sleep(0.01)
print("Sweep from 180 to 0")
for i in range(180):
    servo.angle = 180 - i
    time.sleep(0.01)
