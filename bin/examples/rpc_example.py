from rpc_sender import get_resource
import time

RECEIVER = "http://mac15.home:8080"

# dispatch calls to test object (responds with arguments)
tobj = get_resource(RECEIVER, "TestObj")
print("tobj", tobj)
print("tobj.id", tobj.resource_id)
print("1", tobj.print_args())
print("2", tobj.print_args(1, 2, 3))
print("3", tobj.print_args('hey', [1,23], {'a':5, 'x': 'abc'}, foo='bar', five=5))
print("4", tobj.print_args(stuff=5))

# remotely operate Rigol DP832A power supply

pwr = get_resource(RECEIVER, "pwr")
print("pwr", pwr)

# temperature ...
print("temp = {} C".format(pwr.temperature()))

# configuration
print(pwr.config(1, v=12, enabled=False, i=2.5, ocp=2.8, ovp=None))
print(pwr.config(2, v=10, enabled=True, i=0.2, ocp=2.1234, ovp=12))
print(pwr.config(3, enabled=False, ocp=1.7))

# measure outputs
for _ in range(2):
    for ch in [1,2]: print("channel {}:  v = {:8.3f} V,  i={:8.3f} A,  p={:8.3f} W".
        format(ch, pwr.v(ch), pwr.i(ch), pwr.p(ch)))
    time.sleep(1)

pwr.release_resource()
