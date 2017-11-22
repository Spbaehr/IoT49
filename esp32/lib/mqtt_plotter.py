from mqtt import MQTTClient
from json import dumps

class MQTTPlotter:

    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client

    # create a new series on remote
    # all data of a prior series with the same name will be lost
    # arguments:
    #    series name (first)
    #    column names
    def new_series(self, *args):
        self.mqtt_client.publish("new_series", dumps(args))

    # add data to series on remote, use after 'new_series'
    # arguments:
    #    series name
    #    column values (same number as column names submitted wiht new_series)
    def data(self, *args):
        self.mqtt_client.publish("data", dumps(args))

    # store series on remote in pickle format
    def save_series(self, series, filename=None):
        self.mqtt_client.publish("save_series", dumps([ series, filename ]))

    # plot series on remote
    def plot_series(self, series, **kwargs):
        self.mqtt_client.publish("plot_series", dumps([ series, kwargs ]))

    # evaluate python code on remote
    # Beware: security hole!
    # enable in plot_server if desired
    def exec_remote(self, code):
        print("------------ exec_remote:", code)
        self.mqtt_client.publish("exec_remote", dumps(code))
