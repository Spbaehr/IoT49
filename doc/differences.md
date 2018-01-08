# Firmware Differences compared to Standard MicroPython

**This document is outdated**

The goal of this port is to be fully compatible with standard MicroPython, except for additions. Differences are listed below:

1. The firmware uses both cores of the ESP-32. One is dedicated to the user program.
2. `network.telnet` for wireless `repl`.
3. `network.mDNS` server
3. `time.ticks_us` returns a 64-bit result. Standard MicroPython returns a 32-Bit result that overflows overflows each hour, resulting in errors when calculating time differences. The 64-bit output avoids these errors at the expense of incompatibility with `time.ticks_diff` (not needed, do not call) and memory allocation on the heap.
4. Updated `iot49.sleep_us` with better accuracy than `time.sleep_us` and not disabling interrupts.
5. Optional `timer` argument in `machine.PWM`. Allows up to 4 different output frequencies; with standard MicroPython all PWM outputs are at the same frequency.
6. Built-in board module with pin names for HUZZAH32
6. Built-in device drivers for MPU9250, INA219
6. [ESP Now](espnow.md)