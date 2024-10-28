# Original SA.py is from IoTtalk/Dummy_Device_IoTtalk_v1_py (ea33ed9)


import json
import time
import config
import serial
import random 


ServerURL = config.iottalk_server_url #For example: 'https://DomainName'
MQTT_broker = config.mqtt_broker None # MQTT Broker address, for example: 'DomainName' or None = no MQTT support
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


ser = serial.Serial(serial_port, 9600, timeout=1)
ser.open()
red_color = []
green_color = []
default_color = [255, 210, 00]
default_sensor_info = {
    'temperature_control': default_color,
    'humidity_control': default_color,
}

def Dummy_Sensor():
    global ser, red_color, green_color, default_color, default_sensor_info
    sensor_str = ser.read(100)

    if len(sensor_str) == 0:
        return default_sensor_info

    try:
        sensor_info = json.loads(sensor_str)
    except json.decoder.JSONDecodeError:
        return default_sensor_info

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

    time.sleep(1)

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


