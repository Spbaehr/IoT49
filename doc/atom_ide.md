# Atom IDE

## Editor Window

![Atom IDE](atom_ide.png)

The figure shows the Atom IDE with the project file browser at the left (menu `File->Project Folder...` and navigate to the `IoT49/esp32` folder if it is not open), the editing pane at the top right, and the ESP32 REPL console at the bottom right.

## REPL

Commands typed into the REPL console are sent the the ESP32 for execution and results returned to the console for display.

Click `Connect` or `Reconnect` if the REPL prompt (`>>>`) is not displayed. Sometimes it is necessary to press the reset button on the ESP32 and wait ~10 seconds before a connection can be made.

## Editor & Running Code

Clicking on a file in the browser opens an editor window. Choose `File->New File...` and type a few Python commands into the blank editor window.

![Atom IDE](new_file.png)

Click `File->Save` and enter a suitable name and extension **.py**.

![Atom IDE](save_dialog.png)

Make sure the editor window with the code you just typed is selected (you may need to click inside the window) and then click the `Run` button above the REPL window. The code is uploaded and executed on the ESP32 and results sent back for display in the console.

![Atom IDE](run.png)

