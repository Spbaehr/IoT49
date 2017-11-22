import sys
sys.path.append('/Users/boser/Dropbox/Files/Class/49/code/python/lib')

from mqttplotter import MQTTPlotter
from mqttclient import MQTTClient
from collections import OrderedDict
from matplotlib import rc
import matplotlib.pyplot as plt
import json, pickle, os

# Create malab-like plots from data submitted by MQTT
# Usage:
#     import sys
#     sys.path.append('/Users/boser/Dropbox/Files/Class/49/code/python/lib')
#     from mqttclient import MQTTClient
#     from plotserver import PlotServer
#
#     BROKER = "iot.eclipse.org"
#     mqtt = MQTTClient(BROKER)
#     server = PlotServer(mqtt)
#     print("MQTT client started ... waiting for data!")
#     mqtt.loop_forever()   # blocking; see MQTTClient for non-blocking alternatives

class PlotServer:

    def __init__(self, mqtt, qos=0):
        self.series_ = {}
        mqtt.subscribe("new_series", self.new_series_, qos)
        mqtt.subscribe("data", self.data_, qos)
        mqtt.subscribe("save_series", self.save_series_, qos)
        mqtt.subscribe("plot_series", self.plot_series_, qos)
        self.mqtt = mqtt

    # create new series (stored as dict in self.series_)
    def new_series_(self, client, userdata, msg):
        topic = msg.topic
        payload = json.loads(msg.payload)
        series = OrderedDict()
        for c in payload[1:]:
            series[c] = []
        self.series_[payload[0]] = series
        print("new series '{}' with fields {}".format(payload[0], payload[1:]))

    # add data to series defined previously with new_series
    def data_(self, client, userdata, msg):
        topic = msg.topic
        payload = json.loads(msg.payload)
        series = self.series_[payload[0]]
        for i, v in enumerate(series.values()):
            v.extend([payload[i+1]])

    # store series on remote in pickle format
    def save_series_(self, client, userdata, msg):
        topic = msg.topic
        payload = json.loads(msg.payload)
        series = self.series_[payload[0]]
        filename = payload[1]
        if not filename: filename = payload[0] + ".pkl"
        dirname = os.path.dirname(filename)
        if len(dirname) > 0: os.makedirs(dirname, exist_ok=True)
        pickle.dump(series, open(filename, "wb"))
        print("saved series '{}' to file '{}'".format(payload[0], filename))

    # plot series on remote
    def plot_series_(self, client, userdata, msg):
        topic = msg.topic
        payload = json.loads(msg.payload)
        series = self.series_[payload[0]]
        kwargs = payload[1]
        rc('font', **{'family':'serif','serif':['Palatino']})
        rc('text', usetex=True)
        figsize = kwargs.get("figsize", (5, 3))
        fig = plt.figure(figsize=figsize)
        keys = list(series.keys())
        if len(keys) < 1:
            print("series {} has no data to plot!".format(series_name))
            return
        if "hist" in kwargs:
            v = [0] * len(keys)
            l = [0] * len(keys)
            for i, k in enumerate(keys):
                v[i] = series[k]
                l[i] = k
            plt.hist(v, histtype='bar', stacked=False, rwidth=0.7, label=l)
        else:
            x = series[keys[0]]
            if len(keys) < 2:
                plt.plot(x, label=keys[0])
            else:
                keys.pop(0)
                fmt = kwargs.get("format", [])
                for i, y in enumerate(keys):
                    f = fmt[i] if len(fmt) > i else ''
                    plt.plot(x, series[y], f, label=y)
        if "title"  in kwargs: plt.title(kwargs["title"])
        if "xlabel" in kwargs: plt.xlabel(kwargs["xlabel"])
        if "ylabel" in kwargs: plt.ylabel(kwargs["ylabel"])
        plt.xscale("log" if kwargs.get("xlog", False) else "linear")
        plt.yscale("log" if kwargs.get("ylog", False) else "linear")
        plt.grid(kwargs.get("grid", True))
        if len(keys) > 1: plt.legend()
        filename = kwargs.get("filename", payload[0] + ".pdf")
        dirname = os.path.dirname(filename)
        if len(dirname) > 0: os.makedirs(dirname, exist_ok=True)
        plt.savefig(filename, bbox_inches="tight")
        plt.close(fig)
        print("saved plot of series '{}' to file '{}'".format(payload[0], filename))
