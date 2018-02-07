## Determine USB Port Name

### OSX/Linux

Open a terminal window (search `Terminal` from the command bar and click on the appropriate result) and type `ls /dev` at the prompt. You will be presented with a long list of device names. The one you are looking for likely contains the string `USB`. Try `ls /dev/*USB*` to get a list of only those devices. Likely the name you are looking for is `/dev/cu.SLAB_USBtoUART` (`/dev/ttyUSB0` on Linux). Unplug the ESP32 and run `ls /dev/*USB*` again. If the device is no longer present in the listing it is the one you are looking for.

**Linux:** On Linux, the user may need to be added to the dialout group to have access to the USB port without being root. E.g. on Ubuntu, run `sudo usermod -a -G dialout $USER`.

### Windows

To find out what the USB (also called COM-port on Windows) is, open the Windows `Device Manager`. Click the Windows button (typically in the lower left of the corner of the screen) and type `device` in the search box. Click `Device Manager`. Connect the ESP32 microcontroller to a free USB port. Then open the tab `Ports (COM & LPT)` in the device manager. Look for the line starting with `Silicon Labs CP210x`. The port you are looking for is listed in parentheses at the end of the line, e.g. `COM3`. Take note of this value, you will need it to program the microcontroller.

**Note:** Port names sometimes change, e.g. when other USB devices are connected to the computer. If the connection fails, repeat the procedure described above to determine the correct port name.
