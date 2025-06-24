from microbit import *
import radio

radio.config(group=42)
radio.on()
compass.calibrate()

beacon_direction = 0

while True:
    incoming = radio.receive()
    if incoming == "beacon":
        heading = compass.heading()
        diff = (heading - beacon_direction + 360) % 360

        if diff < 15 or diff > 345:
            display.show(Image.YES)
            sleep(500)
        elif 165 < diff < 195:
            display.show(Image.NO)
            sleep(500)
        elif 15 <= diff < 180:
            display.show(Image.ARROW_W)
            sleep(500)
        else:
            display.show(Image.ARROW_E)
            sleep(500)
    else:
        display.clear()
