# IoT49 ESP32 Firmware Built-In Modules

The port includes the following modules in addition the standard [MicroPython library](http://docs.micropython.org/en/latest/pyboard/library/index.html):

* iot49: Experimental features
  * `network.telnet` for wireless `repl`.
  * `network.mDNS`
  * [`mqttclient`](https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/umqtt/simple.py)
  * [`plotclient`](https://github.com/bboser/iot-plot)
  * `urequests` subset of standard Python `request` library
  * `ranges` (`linrange`, `logrange`) utility functions
  * Device drivers:
     * `board` HUZZAH32 pin names
     * [`ads1x15`](https://github.com/robert-hh/ads1x15) ADC
     * [`ina219`](https://github.com/chrisb2/pyb_ina219) [high-side current monitor](http://www.ti.com/product/INA219)
     * [`mcp4725`](https://github.com/wayoda/micropython-mcp4725) DAC
     * [`mpu9250`](https://github.com/micropython-IMU/micropython-mpu9x50) [IMU](https://www.invensense.com/products/motion-tracking/9-axis/mpu-9250/)
     * [`ssd1306`](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py) Display
     * `vl5310x` LIDAR
  * `iot49` module, experimental features
     * `version()` - version string
     * `sleep_us(us)` - same as `time.sleep_us(us)` except that interrupts are handled
     * [ESP Now](espnow.md)
