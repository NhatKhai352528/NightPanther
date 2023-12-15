from tkinter import Tk
from typing import Any
from ..Pages.Starts.NPWelcome import NPWelcome


class NPStarts:
    
    def __init__(self, master: Tk, controlCommands: list[Any] = None):
        
        self._master = master
        self._controlCommands = controlCommands
        
        # Pages
        self._welcome = None
    
    def place(self):
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