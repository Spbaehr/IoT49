#! /usr/bin/env python3

import os

iot_dir = os.getenv('IoT49', os.path.join(os.path.expanduser('~'), 'IoT49'))
fw_dir  = os.path.join(iot_dir, 'firmware/dist')
port = os.getenv('RSHELL_PORT')

with open(os.path.join(fw_dir, 'flash_cmd'), 'r') as f:
    flash_parameters = f.read()

flash_cmd = "esptool.py --port {} {}".format(port, flash_parameters)

print('Flash MicroPython to ESP32')
print('Home directory:           ', os.path.expanduser('~'))
print('IoT49 root:               ', iot_dir)
print('Firmware directory:       ', fw_dir)
print('USB Port:                 ', port)
print()
print('Flash parameters:         ', flash_parameters)
print()
print('Flash command:            ', flash_cmd)
print()

os.chdir(fw_dir)
print('Flashing .........................................................')
os.system(flash_cmd)
