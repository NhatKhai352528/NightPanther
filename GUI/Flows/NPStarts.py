from tkinter import Tk
from threading import Thread
from typing import Any
from ..Pages.Starts.NPWelcome import NPWelcome
import globals
import socket

class NPStarts:
    
    def __init__(self, master: Tk, controlCommands: list[Any] = None):
        
        self._master = master
        self._controlCommands = controlCommands
        
        # Pages
        self._welcome = None
    
    def place(self):
        startConnection = Thread(target = self._startConnection)
        startConnection.start()
        self._welcome = NPWelcome(master = self._master, commands = self._controlCommands)
        self._welcome.place()
    
    def destroy(self):
        attributes = ["_welcome"]
        for attribute in attributes:
            try:
                getattr(self, attribute).destroy()
            except:
                pass
        self.__dict__.clear()

    def _startConnection(self):
        globals.ipcPort = 2020
        globals.ipcSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        globals.ipcSocket.bind(('', globals.ipcPort))
        globals.ipcSocket.listen(100)
        (globals.webServerSocket, _) = globals.ipcSocket.accept()