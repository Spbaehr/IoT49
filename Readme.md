# EE49 Micropython Programming Environment 

Firmware and ESP32 MicroPython Programming Environment for UC Berkeley EE49.

## Install

* [OSX (and Linux)](doc/osx.md)
* [Windows](doc/windows.md)

## Firmware
Contains the micropython interpreter and libraries compiled for the ESP-32.

To install, connect ESP-32 via USB to port /dev/ttyUSB0 (on Ubuntu), cd to folder "firmware" and type ./flash.sh at the command prompt.

__Documentation:__

* Micropython: http://www.micropython.org
* Source code: https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo

## Code

### esp32

* boot.py (connect to wifi)
* main.py (stub only)
* lib:
	* ina219: https://github.com/chrisb2/pyb_ina219
	* mpu9250: https://github.com/micropython-IMU/micropython-mpu9x50
	* mqtt: https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/umqtt/simple.py

