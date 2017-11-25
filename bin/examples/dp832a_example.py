import sys
sys.path.append('/Users/boser/Dropbox/Files/Class/49/code/python/lib')

from dp832a import DP832A
import time

# instrument
pwr = DP832A()

# temperature ...
print("temp = {} C".format(pwr.temperature()))

# configuration
print(pwr.config(1, v=12, enabled=False, i=2.5, ocp=2.8, ovp=None))
print(pwr.config(2, v=10, enabled=True, i=0.2, ocp=2.1234, ovp=12))
print(pwr.config(3, enabled=False, ocp=1.7))

# measure outputs
for _ in range(5):
    for ch in [1,2,3]: print("channel {}:  v = {:8.3f} V,  i={:8.3f} A,  p={:8.3f} W".
        format(ch, pwr.v(ch), pwr.i(ch), pwr.p(ch)))
    time.sleep(1)
