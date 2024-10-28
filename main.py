import time
import config
from microbit import *
from version_2 import DHT11


uart.init(config.uart_rate)
while True:
    sensor_info = {
        'temp_control': None,
        'humidity_control': None,
    }

    try:
        sensor = DHT11(pin0)
        temp, humidity = sensor.read()
        sensor_info['temp_control'] = temp
        sensor_info['humidity_control'] = humidity

        print(sensor_info)
        time.sleep(2)
    except:
        time.sleep(3)
    finally:
        sensor_str = '{},{}'.format(sensor_info['temp_control'], sensor_info['humidity_control'])
        uart.write(sensor_str.encode('utf-8'))
