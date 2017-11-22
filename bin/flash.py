#! /usr/bin/env python3

import os

iot_dir = os.getenv('IoT49', os.path.join(os.path.expanduser('~'), 'IoT49')
fw_dir  = os.path.join(iot_dir, 'firmware/dist')
port = os.getenv('RSHELL_PORT')

with open(os.path.join(fw_dir, 'flash_cmd'), 'r') as f:
    flash_cmd = f.read()

cmd = "cd {}; esptool.py --port {} {}".format(fw_dir, port, flash_cmd)

os.system(cmd)
