from dmm34461a import DMM34461A

dmm = DMM34461A()
dmm.help()

print(dmm.config())
for _ in range(1):
    print("config={} value={}".format(dmm.config('dc_volts'), dmm.read()))
    print("config={} value={}".format(dmm.config('ac_volts'), dmm.read()))
    print("config={} value={}".format(dmm.config('resistance'), dmm.read()))
    print("config={} value={}".format(dmm.config('diode'), dmm.read()))
print(dmm.config())

dmm.close()
