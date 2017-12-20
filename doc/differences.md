# Firmware Differences compared to Standard MicroPython

The goal of this port is to be fully compatible with standard MicroPython, except for additions. Differences are listed below:

1. The firmware uses both cores of the ESP-32. One is dedicated to the user program.
2. `network.telnet` for wireless `repl`.
3. `esp.ticks_us` with 64-bit output. `time.ticks_us` returns a 32-bit result which overflows each hour, resulting in errors when calculating time differences. The 64-bit output avoids these errors at the expense of incompatibility with `time.ticks_diff` (not needed, do not call) and memory allocation on the heap.
4. Updated `time.sleep_us` and `time.sleep_ms` with better accuracy and and not disabling interrupts. Except for the improvements use is transparent and compatible with standard MicroPython.
5. Optional `timer` argument in `machine.PWM`. Allows up to 4 different output frequencies; with standard MicroPython all PWM outputs are at the same frequency.