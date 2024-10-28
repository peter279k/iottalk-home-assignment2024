import json
import time
import config
from microbit import *
from version_2 import DHT11


uart.init(config.uart_rate)
while True:
    sensor_info = {
        'temp_control': 0.0,
        'humidity_control': 0.0,
    }

    try:
        sensor = DHT11(pin0)
        temp, humidity = sensor.read()
        sensor_info['temp_control'] = temp
        sensor_info['humidity_control'] = humidity

        print(sensor_info)
        sensor_str = json.dumps(sensor_info)
        uart.write(sensor_str.encode('utf-8'))

        time.sleep(2)
    except:
        time.sleep(3)
