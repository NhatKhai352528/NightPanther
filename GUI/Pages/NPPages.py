from tkinter import Tk
from typing import Any
from ..Frames.Workspaces.NPControl import NPControl
from ..Frames.Workspaces.NPData import NPData
from ..Frames.Workspaces.NPInteract import NPInteract

class NPPages:
    
    def __init__(self, master: Tk, commands: list[Any] = None):
        
        self._master = master

        # Passed commands handler
        self._commands = [Any, Any]
        for i in range(2):
            try:
                self._commands[i] = commands[i]
            except:
                self._commands[i] = None
        
        self._data = NPData(master = self._master)
        self._control = NPControl(master = self._master)
        self._interact = NPInteract(master = self._master)
    
    def place(self):
        self._data.place()
        self._control.place()
        self._interact.place()
    
    def place_forget(self):
        self._data.place_forget()
        self._control.place_forget()
        self._interact.place_forget()
    
    def destroy(self):
        self._data.destroy()
        self._control.destroy()
        self._interact.destroy()
        self.__dict__.clear()
        