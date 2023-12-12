from tkinter import Tk
from typing import Any
from ..Pages.Admins.NPVerify import NPVerify

class NPAdmins:
    
    def __init__(self, master: Tk, destroyCommand: Any):
    
        self._master = master
        self._destroyCommand = destroyCommand
        
        # Pages
        self._verify = None
        
    def place(self):
        self._verify = NPVerify(master = self._master, commands = [self._destroyCommand, None])
        self._verify.place()
    
    def destroy(self):
        attributes = ["_verify"]
        for attribute in attributes:
            try:
                getattr(self, attribute).destroy()
            except:
                pass
        self.__dict__.clear()