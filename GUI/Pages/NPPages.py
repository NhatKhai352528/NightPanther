from tkinter import Tk
from ..Frames.Workspaces.NPControl import NPControl
from ..Frames.Workspaces.NPData import NPData
from ..Frames.Workspaces.NPInteract import NPInteract
from ..Frames.Workspaces.NPWorkspace import NPWorkspace

class NPPages:
    
    def __init__(self, master: Tk):
        
        self._master = master
        self._workspace = NPWorkspace(master = self._master)
        self._mainFrame = self._workspace.npget(attribute = "frame")
        
        self._data = NPData(master = self._mainFrame)
        self._control = NPControl(master = self._mainFrame)
        self._interact = NPInteract(master = self._mainFrame)
        
        self._data.place()
        self._control.place()
        self._interact.place()
    
    def place(self):
        self._workspace.place()
    
    def place_forget(self):
        self._workspace.place_forget()
    
    def destroy(self):
        self._workspace.destroy()
        self.__dict__.clear()
        