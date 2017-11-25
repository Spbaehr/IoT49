# IoT49 Micropython Programming Environment 

Firmware and [ESP32](https://esp32.com) [MicroPython Programming](http://www.micropython.org) Environment for [UC Berkeley](http://www.berkeley.edu) EE49. See [https://github.com/bboser/IoT49](https://github.com/bboser/IoT49) for updates.

## Installation

* [OSX (and Linux)](doc/osx.md)
* [Windows](doc/windows.md)

## Contents

### LICENSE
All contents herein are licensed under the [MIT license](LICENSE).

### Firmware
Contains the micropython interpreter and libraries compiled for the ESP-32.

* [Micropython](http://www.micropython.org)
* [Firmware Source Code and Documentation](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo)

### esp32

ESP32 MicroPython code and libraries. The folder `mcu` contains the files that get actually uploaded to the controller and include:

* [boot.py](esp32/mcu/boot.py) (initializations and connect to wifi)
* [main.py](esp32/mcu/main.py) (stub only, replace this with your own code)
* lib:
	* [board](esp32/mcu/lib/board.py): declarations of GPIO pin names
	* [ina219](https://github.com/chrisb2/pyb_ina219): high side current sensor
	* [mpu9x50](https://github.com/micropython-IMU/micropython-mpu9x50): 9 DOF IMU
	* [mqtt](https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/umqtt/simple.py): MQTT client library
	* [mqtt_plotter](): MQTT remote plotting library

### bin

Host-side python tools.

* [esptool.py](https://github.com/espressif/esptool): low level ESP32 programming tool
* erase_flash.py: erases the flash of an ESP32 connected by USB
* flash.py: uploads the MicroPython firmware to the ESP32 connected by USB
* sync.py: uploads the contents of the local esp32/mcu folder to the ESP32 flash memory. Based on [rshell](https://github.com/dhylands/rshell).
* mac.py: inquires and prints the mac address of the ESP32
* run.py: executes the Python code of the file argument. E.g. `run.py hello.py` uploads `hello.py` to the ESP32 RAM, executes the code, and sends the results back to the host
* [start_plotserver.py](): runs a server on the host computer that accepts and executes plotting commands issued on the ESP32 (example: [bin/examples/mqtt_plotter_example.py](bin/examples/mqtt_plotter_example.py))
* [rpc_receiver.py](): dispatches calls from a remote to objects on the server. E.g. control test instruments from ESP32 (example: [bin/examples/rpc_example.py](bin/examples/rpc_example.py))
* LXI Control of [Rigol DP832A power supply](bin/examples/dp832a_example.py), [Keysight DSOX2024A oscilloscope](bin/examples/dsox2024a_example.py), [Keysight DMM34461A multimeter](bin/examples/dmm34461a_example.py)