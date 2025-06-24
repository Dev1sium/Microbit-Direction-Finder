from microbit import *
import radio

radio.config(group=42)
radio.on()
compass.calibrate()

while True:
    heading = compass.heading()
    if heading < 10 or heading > 350:
        display.show(Image.YES)
        break
    else:
        display.show(Image.NO)
    sleep(100)

while True:
    radio.send("beacon")
    display.show(Image.HEART)
    sleep(500)
