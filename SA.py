# Original SA.py is from IoTtalk/Dummy_Device_IoTtalk_v1_py (ea33ed9)


import time
import config
import serial
import random


ServerURL = config.iottalk_server_url #For example: 'https://DomainName'
MQTT_broker = config.mqtt_broker # MQTT Broker address, for example: 'DomainName' or None = no MQTT support
MQTT_port = config.mqtt_port
MQTT_encryption = config.mqtt_encryption
MQTT_User = config.mqtt_user
MQTT_PW = config.mqtt_password

device_model = 'Dummy_Device'
IDF_list = ['Dummy_Sensor']
ODF_list = ['Dummy_Control']
device_id = None #if None, device_id = MAC address
device_name = None
exec_interval = 1  # IDF/ODF interval


ser = serial.Serial(config.uart_port, config.uart_rate, timeout=1)
red_color = [255, 0, 0]
green_color = [0, 128, 0]
default_color = [255, 210, 00]
default_sensor_info = {
    'temperature_control': default_color,
    'humidity_control': default_color,
}

def Dummy_Sensor():
    global ser, red_color, green_color, default_color, default_sensor_info
    sensor_str = ser.read(200)
    sensor_str = sensor_str.decode('utf-8')
    sensor_str = sensor_str.split(',')
    print(sensor_str)

    if len(sensor_str) != 2 or sensor_str[0] == 'None' or sensor_str[1] == 'None':
        return default_sensor_info

    sensor_info = {
        'temperature_control': float(sensor_str[0]),
        'humidity_control': float(sensor_str[1]),
    }

    temperature = sensor_info['temperature_control']
    if temperature <= 20 or temperature >= 25:
        sensor_info['temperature_control'] = red_color
    else:
        sensor_info['temperature_control'] = green_color

    humidity = sensor_info['humidity_control']
    if humidity <= 55 or humidity >= 65:
        sensor_info['humidity_control'] = red_color
    else:
        sensor_info['humidity_control'] = green_color

    return sensor_info

def Dummy_Control(data:list):
    print(data[0])

def on_register(r):
    print(f'Device name: {r["d_name"]}')
    '''
    #You can write some SA routine code here, for example:
    import time, DAI
    while True:
        DAI.push('Dummy_Sensor', [100, 200])
        time.sleep(exec_interval)
    '''
