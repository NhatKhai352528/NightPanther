from tkinter import Tk
from typing import Any, Literal, Optional
from ..Pages.Settings.NPPrimary import NPPrimary

class NPSettings:
    
    def __init__(self, master: Tk, destroyCommand: Any):
    
        self._master = master
        self._destroyCommand = destroyCommand
        
        # Pages
        self._primary = None
        
        self._pages = Literal["_primary"]
        self._currentPage: Optional[self._pages] = None
        
    def place(self):
        if self._currentPage == None:
            self._initPrimary()
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
    
    def _initPrimary(self):
        self._primary = NPPrimary(master = self._master, commands = [self._destroyCommand, None])
        self._primary.place()
        self._currentPage = "_primary"