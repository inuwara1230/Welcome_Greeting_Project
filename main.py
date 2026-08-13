import time
import neopixel
import os
from machine import I2S,Pin

#ledpin = machine.Pin(16, machine.Pin.OUT)
#pixels = neopixel.NeoPixel(ledpin, 1)

BCLK_PIN = 10
LRC_PIN = 11
DATA_PIN = 12

audio_out = I2S(
    0,
    sck=Pin(BCLK_PIN),
    ws=Pin(LRC_PIN),
    sd=Pin(DATA_PIN),
    mode=I2S.TX,
    bits=16,
    format=I2S.MONO,
    rate=48000,
    ibuf=20000
)

#print("I2S initialized")

print(f"files: {os.listdir()}")
time.sleep(5)

try:
    with open("cs1.wav", "rb") as f:
        #print("file loaded")
        
        f.seek(44)

        while True:
            data = f.read(1024)
            if not data:
                break
            audio_out.write(data)
    #print("Playback finished")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    audio_out.deinit()