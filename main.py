import globals
import socket
globals.ipcPort = 2020
globals.ipcSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
globals.ipcSocket.bind(('', globals.ipcPort))
globals.ipcSocket.listen(100)
(globals.webServerSocket, _) = globals.ipcSocket.accept()

import GUI.gui


