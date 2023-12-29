import platform
import globals

if platform.system() == "Windows":
    globals.runningMode = "Debug"
else:
    globals.runningMode = "Release"  
    import socket
    globals.ipcPort = 2020
    globals.ipcSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    globals.ipcSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    globals.ipcSocket.bind(('', globals.ipcPort))
    globals.ipcSocket.listen(100)
    (globals.webServerSocket, _) = globals.ipcSocket.accept()

import GUI.gui
