# Install the uPython Programming Environment

These instructions have been tested on *macOS Sierra* Version 10.12.6 and Windows 10. The installation on Linux is similar with a few changes depending on the version of Linux you are using.

Read the entire document before starting the installation.

## 1) Install the USB Driver

Download and install the CP210X USB driver from [https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers).

For windows there are two versions: `x64` is for newer 64-Bit CPUs, while `x86` is for 32-Bit computers. Pick the right one for your computer. Unless it is quite old, that's likely `x64`. All Mac's are 64-Bit.

**Important:** For later steps you will need to know the name of the port of the USB device. To find out what it is, connect the ESP32 microcontroller to a free USB port.

### OSX/Linux

Open a terminal window (search `Terminal` from the command bar and click on the appropriate result) and type `ls /dev` at the prompt. You will be presented with a long list of device names. The one you are looking for likely contains the string `USB`. Try `ls /dev/*USB*` to get a list of only those devices. Likely the name you are looking for is `/dev/cu.SLAB_USBtoUART` (`/dev/ttyUSB0` on Linux). Unplug the ESP32 and run `ls /dev/*USB*` again. If the device is no longer present in the listing it is the one you are looking for.

**Linux:** On Linux, the user may need to be added to the dialout group to have access to the USB port without being root. E.g. on Ubuntu, run `sudo usermod -a -G dialout $USER`.

### Windows

To find out what the USB (also called COM-port on Windows) is, open the Windows `Device Manager`. Click the Windows button (typically in the lower left of the corner of the screen) and type `device` in the search box. Click `Device Manager`. Connect the ESP32 microcontroller to a free USB port. Then open the tab `Ports (COM & LPT)` in the device manager. Look for the line starting with `Silicon Labs CP210x`. The port you are looking for is listed in parentheses at the end of the line, e.g. `COM3`. Take note of this value, you will need it to program the microcontroller.

Be sure to always connect the ESP32 to the same physical USB port as the port number may be different for other connectors. The port number can also change when other devices are plugged into different USB ports. If in doubt or in case of problems you can always repeat the steps outlined above to check if the USB port has changed.

### Note

Installing drivers requires typically *Administrator Privileges*. On the EECS IoT49 Lab computers the USB driver has already been installed for you.


## 2) Install Python 3

Determine if Python is already installed. Open a terminal/command window and type:

```
python --version
```

If you get something similar to

```
Python 3.6.3 :: ...
```

Python is already installed. The number after the word `Python` is the version. Verify that it is `3.4` or later. If not, you need to install a newer version.

You can [download Python 3](https://www.python.org/downloads/) from the official Python website. Other installers (e.g. `homebrew` on the Mac or `anaconda`) work as well.

Open a terminal window and type `python` at the prompt. Verify that Python announces itself with the correct version (3.6 or later). Type `exit()` to quit the Python interpreter.

## 3) Install `shell49`

Navigate to [https://github.com/bboser/shell49](https://github.com/bboser/shell49) and follow the instructions to install `shell49`.

## 4) Flash the MicroPython Firmware to the ESP32

Make sure the ESP32 is **not connected to the computer**. At the command prompt type

```
shell49
```

After the greeting, enter the commands below. Replace `<port>` with the USB port determined in step 1 of these instructions, e.g. `/dev/cu.SLAB_USBtoUART` and `<alphanumeric_name>` with a unique name, e.g. `donald_duck` if your name is Donald Duck.

```
config --default port <port>
config --default board HUZZAH32
config --default time_offset 0
```

Now connect the ESP32 to the computer with a USB cable. At the `shell49` prompt type

```
flash -e
```

This flashes the MicroPython firmware to the ESP32. Check for error messages. If there are none, press the reset button on the HUZZAH32 board, then type (replace `<alphanumeric_name>` with the name you want to give your computer - choose something unique like your pets name):

```
config -u name <alphanumeric_name>
repl
```

You should be getting a `REPL prompt` from MicroPython running on the ESP32. Try a few Python commands, e.g.

```
1+1
2**100
for i in range(4):
    print(i, i**2)
from machine import Pin
from board import LED
led = Pin(LED, mode=Pin.OUT)
led(1)
```

See how the microcontroller lights up the world ...

```
led(0)
```

to conserve energy.

When you are done experimenting, type `Ctrl-X` followed by `Ctrl-D` to exit `shell49`.

## 6) Get a Text Editor

To write programs you need a text editor. Any plain text editor works (e.g. `TextEdit` or `Notepad`), but an editor with Python syntax highlighting helps catching errors.

A [web search](https://wiki.python.org/moin/PythonEditors) brings up many options to choose from. If you are already familiar with a suitable editor, use it.

If you prefer an ```Integrated Programming Environment (IDE)``` which  keeps track of your project, you might consider the [Atom Editor](https://atom.io).

`Atom` comes with a wide range of optional plug-ins with useful features. E.g. `linter-pyflakes` points out Python syntax errors in the editor.

The `Pymakr` plugin can be used as an alternative to `shell49` to upload and run code from the editor to the microcontroller. [Installation](https://docs.pycom.io/chapter/pymakr/installation/atom.html) and [usage](atom_ide.md) instructions can be found on the web.

![Atom IDE Screenshot](atom_cuSLAB.png)
