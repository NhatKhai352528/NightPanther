from tkinter import Tk
from typing import Any, Literal, Optional
from ..Pages.Starts.NPWelcome import NPWelcome


class NPStarts:
    
    def __init__(self, master: Tk, controlCommands: list[Any] = None):
        
        self._master = master
        self._controlCommands = controlCommands
        
        # Pages
        self._welcome = None
        
        self._pages = Literal["_welcome"]
        self._currentPage: Optional[self._pages] = None
    
    def place(self):
        if self._currentPage == None:
            self._initWelcome()
        else:
            getattr(self, self._currentPage).place()
    
    def place_forget(self):
        if self._currentPage != None:
            getattr(self, self._currentPage).place_forget()
    
    def destroy(self):
        for page in self._pages.__args__:
            try:
                getattr(self, page).destroy()
            except:
                pass
        self.__dict__.clear()
    
    def _initWelcome(self):
        self._welcome = NPWelcome(master = self._master, commands = self._controlCommands)
        self._welcome.place()
        self._currentPage = "_welcome"
        