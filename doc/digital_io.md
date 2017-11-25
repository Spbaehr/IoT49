# Digital GPIO

## Output

All pins named A0 ... A21 **except A2, A3, A4** can be used for digital output.

### Standard Output
In standard mode, the pin is driven to GND (0V) or VDD (3.3V) depending on its state.

```python
from machine import Pin
p = Pin(id, mode=Pin.OUT)
p(0)   # pin driven to 0V
p(1)   # pin driven to VDD (~ 3.3V)

```
`id` is the name of the pin, e.g. `A0`.

### Open Drain Output
When configured as open drain, a pin is pulled low (tied to GND through approximately 35 Ohm) when set to 0, and open when set to 1.

```python
from machine import Pin
p = Pin(id, mode=Pin.OPEN_DRAIN)
p(0)   # pin driven to 0V
p(1)   # pin open (not driven)

```
`id` is the name of the pin, e.g. `A0`.

## Input

## PWM

## Interrupts