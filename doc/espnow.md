# ESP NOW

* [Guide](http://espressif.com/sites/default/files/documentation/esp-now_user_guide_en.pdf)
* [Docs](http://esp-idf.readthedocs.io/en/latest/api-reference/wifi/esp_now.html)
* [More docs](https://github.com/espressif/esp-idf/blob/master/docs/api-reference/wifi/esp_now.rst)
* [API, chapter 3.8](esp8266_non_os_sdk_api_reference_en.pdf)
* [Nick Zoic's Pull Request](https://github.com/micropython/micropython-esp32/pull/226)

Example:

```python
import network
import esp
w = network.WLAN()
w.active(True)
esp.espnow.init()
bcast = bytes([255,255,255,255,255,255])
esp.espnow.add_peer(w, bcast)
esp.espnow.set_recv_cb(lambda x: print("RECV %s %s" % x))
esp.espnow.set_send_cb(lambda x: print("SEND %s %s" % x))
esp.espnow.send(bcast, "hello, world")
```