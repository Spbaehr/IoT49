# Install uPython on Windows

These instructions have been tested on Windows 10 and may need adjustments on other versions of Windows.

## 1) Install the USB Driver

This step requires *Administrator Privileges*. On the EECS IoT49 Labs computers the USB driver has already been installed for you.

Download and install the CP210X USB driver from [https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers). Choose the default version (not the one with Serial Enumeration).

**Important:** For later steps you will need to know the `COM` port of the USB device. To find out what it is, open the Windows `Device Manager`. Click the Windows button (typically in the lower left of the corner of the screen) and type `device` in the search box. The click `Device Manager`. 

Connect the ESP32 microcontroller to a free USB port. Then open the tab `Ports (CMO & LPT)` in the device manager. Look for the line starting with `Silicon Labs CP210x`. The port you are looking for is listed in parantheses at the end of the line, e.g. `COM3`. Be sure to always connect the ESP32 to the same USB port as the port number may be different for other ports. 

## 2) Install Python 3

Download and install [Python 3.6](https://www.python.org) from [https://www.python.org](https://www.python.org).

In the installer window, make sure that `Install launcher` and `Add Python 3.6 to PATH` are checked.

Bring up an Command Prompt (click the Windows or Start button, type `cmd` and click `Command Prompt`).

At the command prompt type `python`. Verify that Python announces itself with the correct version (3.6). Type `exit()` to quit the Python interpreter.

Back at the Windows Command Prompt, issue the following instructions to install additional packages:

```
pip install pyserial
pip install matplotlib
```

## 3) Download the Programming Environment

Install `git` from [https://git-for-windows.github.io](https://git-for-windows.github.io). Accept the default options.

Click the Windows button and type `git` in the search field. Click on `Git Bash`. In the window that opens type the following command:

```
git clone https://github.com/bboser/IoT49.git
```

This downloads the `IoT49 MicroPython programming environment` to the hard drive of your computer.

If you ever need to update the environment, open a `Git Bash` window and enter the following commands:

```
cd IoT49
git pull
git submodule update --init --recursive
``` 

## 4) Update the Command Search Path

Click the Windows button and type `env`, then click `Edit environment variables for your account`.

Under `User variables for ...`, select `Path` and click `Edit...`. Click new and enter the path where you copied the EE49 Programming Environment, followed by `\bin`. E.g. `C:\Users\joe\IoT49\bin`. Click `OK`.

Back to the screen showing `User variables for ...`, select `New` to create the following environment variables (update the values to reflect your setup):

Variable      | Value
------------- | -------------
PYTHONPATH    | COM3
RSHELL_PORT   | C:\Users\joe\IoT49\bin\lib

Hit `OK` a couple of times to quit the variable editor. Close and reopen all Command Prompt Windows to update them to the new environment you just set.

## Flash the MicroPython Firmware to the ESP32

Connect the ESP32 to the computer via USB. Open a Windows `Command Prompt` and type 

```
flash.py
sync.py
```

The first command installs the MicroPython interpreter on the ESP32. `sync.py` copies Python library files to the microcontroller. You also use this program to copy Python code you wrote to the flash memory on the controller.

## Install the Atom IDE

Download and install the [Atom Editor](https://atom.io) from {https://atom.io}(https://atom.io). Once installed, start the editor by clicking on the green icon on the desktop. Choose `File->Settings` and click on `+ Install`. Search for `pymakr`. Scroll down to the package with name `Pymakr` in click the install button.

From `File` choose `Add Projects Folder...`. Navigate to `C:\Users\joe\IoT49\esp32` and click `Select Folder`.

After `Pymakr` is downloaded and installed, a window appears near the bottom of the Atom IDE. Click `Settings->Project Settings` and edit the value of the field `"address"` to match the USB port the ESP32 is connected to (e.g. `COM3`). Click `Connect`. If all goes well, the ESP32 announces itself by printing the version of the installed firmware (e.g. `IoT49-2017-11-12`). The `>>>` indicates the interpreter is ready to accept commands. Try `5-9`. It can also do harder calculations, and execute complex Python commands. Try!




