from machine import Timer
import machine
import utime
import ledBlink


sensor_temp = machine.ADC(4) #gets info from correct sensor
conversion_factor = 3.3 / (65535) #IDK 
durration = 10 #get Temperature every 60 seconds
time = Timer()

#reads temperature from sensor
def temperature():
    reading = sensor_temp.read_u16() * conversion_factor 
    temperatureCelsius = 27 - (reading - 0.706)/0.001721 #Temperature in celsius
    return temperatureCelsius


def main():
    while True: #Endless loop    
        formatedTemp = "{temp:.2f}"
        ledBlink.blink(2)
        print(formatedTemp.format(temp = temperature()))
        utime.sleep(durration)



if __name__ == "__main__":
    main()