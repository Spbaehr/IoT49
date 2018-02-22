# Digital GPIO

* [Output](#output)
* [Input](#input)
* [PWM](#pwm)
* [Encoder](#encoder)
* [Interrupts](#interrupts)
* [Timers](#timers)

## <a name="output">Output</a>

All pins named A0 ... A21 **except `A2, A3, A4`** can be used for digital output.

### Standard Output
In standard mode, the pin is driven to GND (0V) or VDD (3.3V) depending on its state.

```python
from machine import Pin
p = Pin(id, mode=Pin.OUT)
p(0)   # pin driven to 0V
p(1)   # pin driven to VDD (~ 3.3V)

```
`id` is the name of the pin, e.g.

```python
from board import A0
from machine import Pin
p = Pin(A0, mode=Pin.OUT)
```

### Open Drain Output
When configured as open drain, a pin is pulled low (tied to GND) when set to `0`, and open when set to `1`.

```python
from machine import Pin
p = Pin(id, mode=Pin.OPEN_DRAIN)
p(0)   # pin driven to 0V
p(1)   # pin open (not driven)

```
`id` is the name of the pin, e.g. `A0`.

## <a name="input">Input</a>
All pins named A0 ... A21 can be configured for digital input.

```python
from machine import Pin
p = Pin(id, mode=Pin.IN)
p()   # 0 if voltage is close to 0V
      # 1 if voltage is close to VDD (3.3V)

```
`id` is the name of the pin, e.g. `A0`.

Optionally, a pull-up or pull-down resistor can be enabled on the pin. This feature is not available on pins `A2, A3, A4`.

```python
from machine import Pin
p = Pin(id, mode=Pin.IN, pull=<None|Pin.PULL_UP|Pin.PULL_DOWN>)
```

For example,

```python
from board import A21
from machine import Pin
p = Pin(A21, mode=Pin.IN, pull=Pin.PULL_UP)
```
configures pin `A21` as an input and connects a pull-up resistor between the input pin and VDD.

The values of the pull-down and pull-up resistors vary from chip-to-chip and pin-to-pin and are tpically 30 ... 80 kOhm (pull-up) and ~17 kOhm (pull-down).

## <a name="pwm">PWM</a>

[Documentation](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/pwm)

Note that even with duty=100 the output goes low for a brief period.

## <a name="encoder">Encoder</a>

The ESP32 has 8 pulse 16-Bit count units, either for quadrature or single input encoders.

Quadrature input 4-phase counting (counts *up or down* in raising and falling edges of `p1` and `p2`):
```python
from machine import Pin, ENC
p1 = Pin(id1, mode=Pin.IN, ...)
p2 = Pin(id2, mode=Pin.IN, ...)
enc = ENC(<unit>, p1, p2)
```

Single input counting (counts *up* on raising and falling edge of `p`):
```python
from machine import Pin, ENC
p = Pin(id1, mode=Pin.IN, ...)
enc = ENC(<unit>, p1)
```

`<unit>` 0 ...7 is the pulse count unit number.

Available functions:
```Python
enc.count()                # returns the current count
enc.cound_and_clear()      # returns the current count and sets the counter to 0
enc.clear()                # sets the counter value to 0
enc.pause()                # pauses counting
enc.resume()               # resumes counting
```

**Note:** the counters are signed 16-Bit ints and will roll over.

Example:

```Python
from board import A18, A19, A20, A21
from machine import Pin, ENC

"""
Quadrature Encoder Demo

Pins A18, A20 generate quadrature input, decoded by A19, A20

Connect A18 --> A19
    and A20 --> A21

Ref: https://github.com/dhylands/upy-examples/blob/master/encoder3.py
"""

# Encoder
quadrature = True   # configure for quadrature or single input counting

if quadrature:
    enc = ENC(0, Pin(A19), Pin(A21))
else:
    enc = ENC(0, Pin(A19))

print("Encoder:", enc)

# Quadrature signal generator

q_idx = 0
q_seq = [0, 1, 3, 2]

qa_out = Pin(A18, mode=Pin.OUT)
qb_out = Pin(A20, mode=Pin.OUT)

def set_out():
    va = (q_seq[q_idx] & 0x02) != 0
    vb = (q_seq[q_idx] & 0x01) != 0
    qa_out.value(va)
    qb_out.value(vb)
    print("{} {}   count ={:4d}".format(
        'X' if va else ' ',
        'X' if vb else ' ',
        enc.count()))

def incr():
    global q_idx
    q_idx = (q_idx+1) % 4
    set_out()

def decr():
    global q_idx
    q_idx = (q_idx-1) % 4
    set_out()

# Demo: counts up and down (quadrature==True) or just up (quadrature==False)

enc.clear()
print("      count ={:4d}".format(enc.count()))

for i in range(12):
    incr()
for i in range(24):
    decr()
for i in range(12):
    incr()
```

## <a name="interrupts">Interrupts</a>

Digital inputs can be configured to call a Python function whenever the value changes.

```python
from machine import Pin
p = Pin(id, mode=Pin.IN, ...)
p.irq(handler, trigger=< Pin.IRQ_FALLING | Pin.IRQ_RISING >)
```

`trigger` may be either `Pin.IRQ_FALLING`, `Pin.IRQ_RISING` or `Pin.IRQ_FALLING | Pin.IRQ_RISING` causing the handler to be called when the input changes from `1 to 0`, `0 to 1`, or in either direction.

`handler` is a Python function with one argument (the `pin` that caused the interrupt). E.g.

```python
def irq_handler(pin):
    pass
```

Code in interrupt handlers must be short and not allocate memory (e.g. no floating point arithmetic, print statements, or manipulating lists). If any of these features are required or for longer computations, use the `schedule` function.

Example:

```python
from machine import Pin
from board import LED, A21
from micropython import schedule

led = Pin(LED, mode=Pin.OUT)

# connect a button between pin A21 and GND
button = Pin(A21, mode=Pin.IN, pull=Pin.PULL_UP)

# number of times button was pressed
count = 0

# extended code (print) called from interrupt
def report(pin):
    global count
    if pin() == 0:
        print("> pressed {} times".format(count))
    else:
        print("         < released {} times".format(count))

# interrupt handler
def button_irq_handler(button):
    global count
    if button() == 0: count += 1
    led(1-button())
    # no printing or memory allocation in interrupt handler
    # schedule for later execution (outside interrupt)
    schedule(report, button)

# attach interrupt handler to button pin
button.irq(button_irq_handler, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)

# interrupts occur in the background (concurrent with REPL)
print("Return control to REPL; interrupts continue in background")
```

**Note:** On the ESP32, MicroPython interrupt handlers are scheduled for later execution by the interpreter. Hence memory allocation (heap) is permitted. This comes at the expense of long interrupt latency (~ 1ms).

MicroPython on other boards (e.g. Pyboard) achieve much lower interrupt latency (few us) but prohibit memory allocation in interrupt handlers.

Consult the MicroPython manual for more information about [writing interrupt handlers](http://docs.micropython.org/en/latest/pyboard/reference/isr_rules.html).

## <a name="timers">Timers</a>

[Documentation](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/timer)
