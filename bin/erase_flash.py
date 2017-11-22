#! /usr/bin/env python3

import os

port = os.getenv('RSHELL_PORT')

cmd = "esptool.py --port {} erase_flash".format(port)

os.system(cmd)
