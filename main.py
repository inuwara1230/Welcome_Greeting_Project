import time
import neopixel
import machine

ledpin = machine.Pin(16, machine.Pin.OUT)
pixels = neopixel.NeoPixel(ledpin, 1)

c= True

while c:
    pixels[0] = (255, 0, 0)  
    pixels.write()  
    time.sleep(1) 

    pixels[0] = (0, 255, 0)  
    pixels.write()  
    time.sleep(1)  

    pixels[0] = (0, 0, 255)  
    pixels.write()  
    time.sleep(1)  

    pixels[0] = (0,0,0)  
    pixels.write()  
    time.sleep(1)
    c = False  
