import time
import os
from machine import I2S,Pin

BCLK_PIN = 3 # pin 10 
LRC_PIN = 4 # pin 11
DATA_PIN = 5 #12

#pin declaration

audio_out = I2S(
    0,
    sck=Pin(BCLK_PIN),
    ws=Pin(LRC_PIN),
    sd=Pin(DATA_PIN),
    mode=I2S.TX,
    bits=16,
    format=I2S.MONO,
    rate=44100,
    ibuf=20000
)


print(f"files: {os.listdir()}")
time.sleep(4) 

try:
    with open("only_dolphine.wav", "rb") as f:
        
        f.seek(44)
        while True:
            data = f.read(1024)
            if not data:
                break
            audio_out.write(data)
    
except Exception as e:
    print(f"An error occurred please check again: {e}")
finally:
    audio_out.deinit()