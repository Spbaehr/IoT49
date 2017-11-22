#! /usr/bin/env python3

import os

print(os.getenv('EE49', '.'))
rshell = os.path.join(os.getenv('EE49'), 'bin/lib/rshell32.py')
esp32  = os.path.join(os.getenv('EE49'), 'code/esp32')

os.system("{} -a rsync -v -m {} /flash".format(rshell, esp32))
