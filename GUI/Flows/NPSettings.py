from tkinter import Tk
from typing import Any
from ..Pages.Settings.NPPrimary import NPPrimary

class NPSettings:
    
    def __init__(self, master: Tk, destroyCommand: Any):
    
        self._master = master
        self._destroyCommand = destroyCommand
        
        # Pages
        self._primary = None
        
    def place(self):
        self._primary = NPPrimary(master = self._master, commands = [self._destroyCommand, None])
        self._primary.place()
    
    def destroy(self):
        attributes = ["_primary"]
        for attribute in attributes:
            try:
                getattr(self, attribute).destroy()
            except:
                pass
        self.__dict__.clear()