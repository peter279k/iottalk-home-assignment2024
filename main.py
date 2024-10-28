import json
import time
import config
from microbit import *
from hcsr04 import HCSR04
from version_2 import DHT11


sonar = HCSR04()
uart.init(config.uart_rate)
while True:
    sensor_info = {
        'temp_control': 0.0,
        'humidity_control': 0.0,
        'ping_control': 0.0,
    }
    distance = round(sonar.distance_mm() / 10)
    sensor_info['ping_control'] = distance

    sensor = DHT11(pin0)
    temperature, humidity = sensor.read()
    sensor_info['temp_control'] = temperature
    sensor_info['humidity_control'] = humidity

    print(sensor_info)
    sensor_str = json.dumps(sensor_info)
    uart.write(sensor_str.encode('utf-8'))

    time.sleep(2)
