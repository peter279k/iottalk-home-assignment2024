# It's for running in the Micro:bit v2

import time
import config
from microbit import *
from version_2 import DHT11


uart.init(config.uart_rate)
while True:
    info = None
    try:
        sensor = DHT11(pin0)
        info = sensor.read()
        time.sleep(2)
    except Exception:
        time.sleep(3)
    finally:
        if info is None:
            sensor_str = 'None,None'
        else:
            sensor_str = str(info[0]) + ',' + str(info[1])

        uart.write(sensor_str.encode('utf-8'))
