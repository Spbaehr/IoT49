# IoT49 Micropython Programming Setup

[ESP32](https://esp32.com) [MicroPython](http://www.micropython.org) programming setup for UC Berkeley course [EE49](https://people.eecs.berkeley.edu/~boser/courses/49/overview.html), Electronics for IoT.

## Installation

* [Instructions](doc/install.md)
* [Atom IDE (optional)](doc/atom_ide.md)


## Documentation

* [GPIO (General Purpose Input/Output)](doc/gpio.md)
   * [HUZZAH32 pin diagram](doc/huzzah32_pins.png)
   * [Digital](doc/digital_io.md)
   * [Analog](doc/analog_io.md)

* IOT49 Firmware for HUZZAH32
   * [Micropython](http://www.micropython.org)
   * [Built-In Modules](doc/modules.md)
   * [MicroPython standard library](https://github.com/micropython/micropython-lib)
   * [Source Code](https://github.com/bboser/MicroPython_ESP32_psRAM_LoBo)
   * **Bugs:** report problems as issues in the [github repo](https://github.com/bboser/MicroPython_ESP32_psRAM_LoBo). Include the output from `import iot49; iot49.version()` and a concise description of the problem along with code and instructions for preproducing it.
