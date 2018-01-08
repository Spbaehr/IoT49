# Timer

Timers are used to run code periodically or after some delay.

Example:

```python
from machine import Timer
import time

def timer_cb(timer):
    """Called at intervals set by period."""
    # ... do whatever needs to be done regularly ...
    pass

# timer_cb is called every "period" [ms]
# BUG: timer_cb never called for period > 26 ???
period = 25

timer = Timer(1)
timer.init(period=period, mode=Timer.PERIODIC, callback=timer_cb)

# timer_cb continues to be called at the specified interval
# while doing other work
for _ in range(100):
    time.sleep(0.01)

print("stop timer")
timer.deinit()
```