#! /usr/bin/env python3

import subprocess

code = \
"""
import network, binascii
print('VAR={:s}'.format(binascii.hexlify(network.WLAN(network.STA_IF).config('mac'), ':')))
"""

resp = subprocess.check_output('rshell -n --quiet repl "{}"'.format(" ~ ".join(code.split('\n'))), shell=True).decode("utf-8")

i1 = resp.find('\nVAR=') + 5
i2 = resp.find('\n', i1)

print(resp[i1:i2])
