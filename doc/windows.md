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

At the command prompt type `python`. Verify that Python announces itself with the correct version (3.6) and type the following commands:

```
from os.path import expanduser  
expanduser("~")
```

The result will look similar to 

```
'C:\\Users\\joe'
```

For this example, the home folder is `C:\Users\joe`. Take note of your home folder, then type `exit()` to quit the Python interpreter.

Back at the Windows Command Prompt, issue the following instructions to install additional packages:

```
pip install pyserial
pip install matplotlib
```

## 3) Download the Programming Environment

Navigate to [https://github.com/bboser/IoT49](https://github.com/bboser/IoT49) on github, click `Clone or download` and then `Download ZIP` and `Save`.  

Go to the `Download` folder, click on the downloaded zip file and copy the folder `IoT49-master` to your home (`C:\\Users\\joe` in the example in step 2 above). Rename the folder to `IoT49`.

## 4) Update the Command Search Path

Click the Windows button and type `env`, then click `Edit environment variables for your account`.

Under `User variables for ...`, select `Path` and click `Edit...`. Click new and enter the path where you copied the EE49 Programming Environment, followed by `\bin`. E.g. `C:\Users\joe\IoT49\bin`. Click `OK`.

Back to the screen showing `User variables for ...`, select `New` to create a new environment variable and enter `RSHELL_PORT` for the name and the USB COM port (`COM3` for the example in step 1). 

Hit `OK` a couple of times to quit the variable editor.

## Flash the MicroPython Firmware to the ESP32

Connect the ESP32 to the computer with a USB cable. Start the `Device Manager` (click the windows icon and type `device` in the search field, then click `Device Manager`). Click on the entry `Ports (COM & LPT)` and look for `Silicon Labs CP210x ...`. Look for the COM port number in parantheses at the end of the line (e.g. `COM3`) and make a note of it.

Open a command window and type `flash32 COM3`. Replace `COM3` with the port you found in the previous step.

## Install the Atom IDE

Download and install the [Atom Editor](https://atom.io) from {https://atom.io}(https://atom.io). Once installed, start the editor by clicking on the green icon on the desktop. Choose `File->Settings` and click on `+ Install`. Search for `pymakr`. Scroll down to the package with name `Pymakr` in click the install button.




