# GPIO

| **WARNING** |
|:-----------:|
| The maximum voltage on any pin of the ESP32 is **3.3V**. |
| The maximum current in or out of any GPIO pin is **10mA**. |

The figure below shows the pin naming of the MicroPython port for the Huzzah32. Module `board` declares all pin names. Many pins have aliases. For example, pin `A12` is also called `LED`, reflecting the fact that it is tied to the on-board LED. Some pins have alternate functions, e.g. `SCL` and `SDA` can be used either or general purpose digital I/O or for I2C communication with attached sensors.

E.g. the following code turns on red LED on the Huzzah32 board:

```python
from board import LED
from machine import Pin

led = Pin(LED, mode=Pin.OUT)
led(1)
```

Follow these links for details on [digital](digital_io.md) and [analog](analog_io.md) input and output.

![ESP32 Huzzah32 Pin Names and Functions](huzzah32_pins.png)