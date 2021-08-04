from machine import Pin
import utime

led = Pin(25, Pin.OUT)

def blink(blinks):
    while blinks >= 0:
        led.value(1)
        utime.sleep(.5)
        led.value(0)
        utime.sleep(.5)
        blinks = blinks - 1

def main():
    blink(2)

if __name__ == "__main__":
    main()