#! /usr/bin/env python3

from rshell import pyboard

pyboard.execfile('hello.py', device='/dev/cu.SLAB_USBtoUART')