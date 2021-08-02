import serial
from serial import Serial
import requests

ser = serial.Serial('COM4', 9600) #starts connection with pi pico 

while True:
    temp = ser.readline().decode() #reads output from device and converts from bytes to str
    print(temp)
    requests.post('http://127.0.0.1:8000/growDataAPI/sensor_data/', data = {'temp': temp, 'sensor': 'http://127.0.0.1:8000/growDataAPI/sensor/1/'})
