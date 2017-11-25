from mqttplotter import MQTTPlotter
from mqttclient import MQTTClient
from math import sin, cos, exp, pi

mqtt = MQTTClient("iot.eclipse.org")
mp = MQTTPlotter(mqtt)

# give the series a unique name (in case you create multiple plots)
SERIES = "sinusoid"

# data column names
mp.new_series(SERIES, 'time', 'cos', 'sin', 'sin*cos')

# generate the data
def f1(t): return cos(2 * pi * t) * exp(-t)
def f2(t): return sin(2 * pi * t) * exp(-t)
def f3(t): return sin(2 * pi * t) * cos(2 * pi * t) * exp(-t)
for t in range(200):
    t *= 0.025
    # submit each datapoint to the plot server
    mp.data(SERIES, t, f1(t), f2(t), f3(t))

# save data as pkl document
# see plot_load_pkl.py for an example of loading it back into python
mp.save_series(SERIES)

# create a plot, default dir is $IoT49
mp.plot_series(SERIES,
    filename="bin/examples/mqtt_plotter_example.pdf",
    xlabel="Time [s]",
    ylabel="Voltage [mV]",
    title=r"Damped exponential decay $e^{-t} \cos(2\pi t)$")

# on ESP32:
# disconnect to free up the port
# print("disconnect")
# mqtt.disconnect()

# on other python installations
# wait until all data is transferred or no plot will be generated ...
import time
time.sleep(5)
