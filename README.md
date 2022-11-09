# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [CircuitPython_Servo](#Circuit{ython_Servo)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## CircuitPython_Servo

### Description
I am making a motor spin 180 degrees, with two buttons


### code: 
```python
# Jabari Bright
# CircuitPython Servo
# Pressing one button moves a servo clockwise, pressing the second button moves it back.

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
        for angle in range(0, 180, 9):  # 0 - 180 degrees, 9 degrees at a time
            my_servo.angle = angle 
            time.sleep(0.1)
    else:
        print("BTN is up")
        pass
    if not btn2.value:
        print("BTN2 is down")
        for angle in range(180,0, -9):  # 180 degrees - 0, -9 degrees at a time
            my_servo.angle = angle 
            time.sleep(0.1)
    else:
        print("BTN2 is up")
        pass

    time.sleep(0.1) # sleep for debounce

```
Thanks [Will H](https://github.com/willhunt914/CirclePython) for the code!


### Evidence

https://user-images.githubusercontent.com/71406948/193132815-3492bdfc-6ba2-4faf-86af-ff938ce07ed9.mov




### Wiring

![Capture](https://user-images.githubusercontent.com/71406948/193138836-dee09a13-41f3-43f1-9621-6a9df615ab66.PNG)

### Reflection
This was really hard because I didnt know how to start with the code, but thanks to my fellow classmate [Will H](https://github.com/willhunt914/CirclePython) for the code! I got it done, but another problem to where the motor wouldnt turn right, but thanks to my teacher I got that figured out.





## Hello_CircuitPython

### Description:

### Code:

```python
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
    dot.fill((0, 0,255))

```

### Evidence

![ezgif com-gif-maker](https://user-images.githubusercontent.com/71406948/193141862-44da5cec-7765-4f7d-a916-1f77c3dbe670.gif)


### Wiring
No wiring
### Reflection
it wasnt really hard all you really had to do was copy a code from the assighnment code on canvas:https://cvilleschools.instructure.com/courses/37129/assignments/493863


## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection

