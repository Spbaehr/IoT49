# WiFi

The file `mcu/boot.py` is executed every time the ESP32 boots and contains the code for connecting the the wireless LAN (WiFi).

* To connect to a password connected network (e.g. at your home), add the SSID and password of your network to `known_wifi_nets` in file `mcu/boot.py`. The screen shot below shows an example for a net with SSID `home-SSID` and password `my_very_secret_password`.
* Connecting to the EECS-PSK network requires registering the device. To do so you need the `MAC address` of your ESP32. Type `mac_address()` at the REPL prompt. The text displayed between quotes is the MAC address (e.g. `30:ae:a4:30:81:a8`). Navigate to [https://iris.eecs.berkeley.edu/db/network](https://iris.eecs.berkeley.edu/db/network/) and click the link `Register a Device`. Enter sensible responses to the questions asked (e.g. `MicroPython` for operating system). Service tpically starts after one business.

![`boot.py` customization for WiFi access](boot.png)