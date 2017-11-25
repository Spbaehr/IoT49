#! /usr/bin/env python3

from mqttclient import MQTTClient
from plotserver import PlotServer

BROKER = "iot.eclipse.org"
mqtt = MQTTClient(BROKER)
server = PlotServer(mqtt)
print("MQTT client started ... waiting for data!")
try:
    # blocking; see MQTTClient for non-blocking alternatives
    mqtt.loop_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print('Stopping httpd...\n')
