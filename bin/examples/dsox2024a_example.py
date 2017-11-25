from dsox2024a import DSOX2024A
import matplotlib.pyplot as plt

def plot(x, y):
    fig = plt.figure(figsize=(5, 3))
    plt.plot(x, y)
    plt.savefig("dsox2024a_plot.pdf", bbox_inches="tight")
    plt.close(fig)

dso = DSOX2024A()
dso.reset()         # default configuration

# frequency for waveform generator
freq = 1000

# waveform generator (connect to channel 1 for this demo)
print(dso.waveform_generator(enabled=True,
    waveform='sine',
    duty_cycle_high=20,
    start_phase=1,
    amplitude=0.5, frequency=freq))

# channel 1 configuration
print(dso.channel(1, enabled=True, scale=1, offset=0))

# timebase and trigger
print(dso.timebase(position=0.5e-4, range=5/freq))
print(dso.trigger(source=1, level=1))

# optional, instead of specifiying scale and offset in channel configurations
# enables all connected channels ... (async square wave if ch2 is connected to Demo 2)
dso.autoscale()

# screenshot ...
dso.screenshot(filename="dsox2024a_example.png")

# grab & plot acquired data for channel 1
wf = dso.acquire(1)
plot(wf.t, wf.v)

# return scope to interactive mode
dso.close()
