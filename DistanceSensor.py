import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
red = 0
blue = 0
green = 0
while True:
    try:
       cm = sonar.distance
        print((sonar.distance))
        time.sleep(0.01)
        if cm < 5:
            Mason.fill((255, 0, 0))#red
        if cm > 5 and cm < 12.5:
            red = simpleio.map_range(cm,5,12.5,255,0)
            blue = simpleio.map_range(cm,5,12.5,0,255)
            Mason.fill((red, 0, blue))
        if cm > 12.5 and cm < 20:   
            blue = simpleio.map_range(cm,12.5,20,255,0)
            green = simpleio.map_range(cm,12.5,20,0,255)
         Mason.fill((0, green, blue))
         if cm > 20:
            Mason.fill((0, 255, 0))#green
            except RuntimeError:
                print("Retrying!")
                time.sleep(0.1)