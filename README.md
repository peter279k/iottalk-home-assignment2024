# iottalk-home-assignment2024 (WIP)

## Introduction

This project is for IotTalk course in the NTOU 2024.

## Scenario

The senario is available in the following picture:

![scenario img](https://i.imgur.com/xKHIxxa.png)

## Setup

Before setting this project, we can look at the following result picture:

## Installation

### config.py

1. Creating the `config.py` file and it can refer the `config.py.example` file.
2. To configure the baud rate, it should be `115200`.

### micro:bit

The completed picture about connecting sensors with micro:bit:

### IotTalk

The completed picture about sensors and devices relationship in the IotTalk platform:

### IotTalk joint control function

Every joint function for ODF should change into the following code snippets:

For `temperature_control` x1:

```python
def run(*args):

    return args['temperature_control'][0]
```

For `temperature_control` x2:

```python
def run(*args):

    return args['temperature_control'][1]

```

For `temperature_control` x3:

```python
def run(*args):

    return args['temperature_control'][2]

```

For `humidity_control` x1:

```python
def run(*args):

    return args['humidity_control'][0]

```

For `humidity_control` x2:

```python
def run(*args):

    return args['humidity_control'][1]

```

For `humidity_control` x3:

```python
def run(*args):

    return args['humidity_control'][2]
```

# References

## DHT-11

- https://nkust.gitbook.io/micro-bit/micropython-dht11-du-gan-qi

## HC-SR04 (future work)

- https://nkust.gitbook.io/micro-bit/micropython-chao-yin-bo-hcsr04

## Heart rate monitor (future work)

- https://sensorkit.joy-it.net/en/sensors/ky-039

## MicroPython micro:bit uart

- https://forum.micropython.org/viewtopic.php?t=11746
- https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html#module-microbit.uart

## PySerial for Dummy sensor

- https://pyserial.readthedocs.io/en/latest/pyserial.html
