# iottalk-home-assignment2024 (WIP)

## Introduction

This project is for IotTalk course in the NTOU 2024.

## Scenario

The senario is available in the following picture:

![scenario img](https://i.imgur.com/N6dNOjE.png)

## Setup

Before setting this project, we can look at the following result picture:

## Installation

### config.py

Creating the `config.py` file and it can refer the `config.py.example` file.

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

For `ping_control` x1:

```python
def run(*args):

    return args['ping_control'][0]
```

For `ping_control` x2:

```python
def run(*args):

    return args['ping_control'][1]
```

For `ping_control` x3:

```python
def run(*args):

    return args['ping_control'][2]
```
