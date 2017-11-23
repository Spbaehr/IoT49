# Install the uPython Programming Environment on the Macintosh

These instructions have been tested on *macOS Sierra* Version 10.12.6 and may need modifications on other versions of MacOS. Read the entire document before starting the installation. 

The installation for Linux is similar with a few changes depending on the version of Linux you are using.

## 1) Install the USB Driver

Download and install the CP210X USB driver from [https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers). 

**Important:** For later steps you will need to know the name of the port of the USB device. To find out what it is, connect the ESP32 microcontroller to a free USB port. Then open a terminal window (search `Terminal` from the command bar and click on the appropriate result) and type `ls /dev` at the prompt. You will be presented with a long list of device names. The one you are looking for likely contains the string `USB`. Try `ls /dev/*USB*` to get a list of only those devices. Likely the name you are looking for is '/dev/cu.SLAB_USBtoUART' (`/dev/ttyUSB0` on Linux). Unplug the ESP32 and run `ls /dev/*USB*` again. If the device is no longer present in the listing it is the one you are looking for.

## 2) Install Python 3

Download and install [Python 3.6](https://conda.io/miniconda.html) from [https://conda.io/miniconda.html](https://conda.io/miniconda.html).

Bring up a Terminal window and type `python` at the prompt. Verify that Python announces itself with the correct version (3.6). Type `exit()` to quit the Python interpreter.

Back at the Windows Command Prompt, issue the following instructions to install additional packages:

```
conda install pyserial
conda install matplotlib
```

## 3) Download the Programming Environment

In a terminal window type

```
cd
git clone https://github.com/bboser/IoT49.git
cd IoT49
pwd
```

This downloads the `IoT49 MicroPython programming environment` to the hard drive of your computer and prints the path where it is installed (e.g. `/Users/joe/IoT49`). Take a note of this path, you will need it in step 4 below.

**Updates:** If you ever need to update the environment, enter the following commands at a terminal window:

```
cd ~/IoT49
git pull
git submodule update --init --recursive
``` 

## 4) Update the Command Search Path and Environment

With a text editor (e.g. TextEdit) open the file `~/.bash_profile` (press `Cmd-Shift-.` to show files with names that start with a period) and add the following lines at the bottom of the file (change `joe` to the correct `joe`):

```
export PATH='/Users/joe/IoT49/bin:$PATH'
export IoT49='/Users/joe/IoT49'
export PYTHONPATH='/Users/joe/IoT49/bin/lib:$PYTHONPATH'
export RSHELL_PORT='/dev/cu.SLAB_USBtoUART'
```

Save your work and close and reopen all terminal windows to let the changes take effect. 

## 5) Flash the MicroPython Firmware to the ESP32

Connect the ESP32 to the computer via USB. Open a Windows `Command Prompt` and type 

```
flash.py
sync.py
```

The first command installs the MicroPython interpreter on the ESP32. `sync.py` copies Python library files to the microcontroller. You also use this program to upload Python code you wrote. If you get a warning from `flash.py` that the firmware could not be installed, try running the command again. If the problem persists, unplug and replug the ESP32 or try a different USB port or computer. Following the instructions in step 1 above, verify that that COM port number is still correct and update the `RSHELL_PORT` environment variable if it has changed.

You can also erase the entire flash of the microcontroller (if something bad happens, e.g. you flashed a program with an infinite loop) by executing `erase_flash.py` from the `Command Prompt`.

**Warning:** Only one USB connection can be active. You may need to quit the Atom IDE (see next section) before using `flash.py` and `sync.py`.

## 6) Install the Atom IDE

Download and install the [Atom Editor](https://atom.io) from {https://atom.io}(https://atom.io). Once installed, start the editor by clicking on the green icon on the desktop. Choose `File->Settings` and click on `+ Install`. Search for `pymakr`. Scroll down to the package with name `Pymakr` in click the install button.

From `File` choose `Add Projects Folder...`. Navigate to `/Users/joe/IoT49/esp32` and click `Select Folder`.

After `Pymakr` is downloaded and installed, the MicroPython command window appears near the bottom of the Atom IDE. Click `Settings->Project Settings` and edit the value of the field `"address"` to match the USB port the ESP32 is connected to (e.g. `cu.SLAB_USBtoUART`). Click `Connect`. 

If all goes well, the ESP32 announces itself by printing the version  (e.g. `IoT49-2017-11-12`) and other details about the installed firmware. 

The `>>>` is the MicroPython prompt. Commands you type here are sent to the ESP32 for execution and the results displayed back here. Try `5-9` or `for i in range(5): print(i**2)`. Have fun exploring!

![Atom IDE Screenshot](atom_screen.png)

