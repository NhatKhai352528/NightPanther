from tkinter import Tk
from typing import Any, Literal, Optional
from ..Pages.Setups.NPA3Price import NPA3Price
from ..Pages.Setups.NPA4Price import NPA4Price
from ..Pages.Setups.NPA5Price import NPA5Price
from ..Pages.Setups.NPOrigin import NPOrigin
from ..Pages.Setups.NPPaper import NPPaper
from ..Pages.Setups.NPSides import NPSides

class NPSetups:
    
    def __init__(self, master: Tk, destroyCommand: Any):
    
        self._master = master
        self._destroyCommand = destroyCommand
        
        # Pages
        self._origin = None
        self._paper = None
        self._sides = None
        self._a3Price = None
        self._a4Price = None
        self._a5Price = None
        
        self._pages = Literal["_origin", "_paper", "_sides", "_a3Price", "_a4Price", "_a5Price"]
        self._currentPage: Optional[self._pages] = None
    
    def place(self):
        if self._currentPage == None:
            self._initOrigin()
        else:
            getattr(self, self._currentPage).place()
    
    def place_forget(self):
        if self._currentPage != None:
            getattr(self, self._currentPage).place_forget()
    
    def destroy(self):
        # attributes = ["_origin", "_paper", "_sides", "_a3Price", "_a4Price", "_a5Price"]
        # for attribute in attributes:
        #     try:
        #         getattr(self, attribute).destroy()
        #     except:
        #         pass
        for page in self._pages:
            try:
                getattr(self, page).destroy()
            except:
                pass
        self.__dict__.clear()
    
    def _initOrigin(self):
        self._origin = NPOrigin(master = self._master, commands = [self._destroyCommand, None], switchCommands = [lambda event = None: self._originToPaper(), lambda event = None: self._originToSides(), lambda event = None: self._originToA3Price(), None])
        self._origin.place()
        self._currentPage = "_origin"
    
    def _originToPaper(self):
        self._paper = NPPaper(master = self._master, commands = [lambda event = None: self._paperToOrigin(), None])
        self._paper.place()
        self._currentPage = "_paper"
        self._origin.place_forget()
    
    def _paperToOrigin(self):
        self._origin.place()
        self._currentPage = "_origin"
        self._paper.destroy()
        self._paper = None
    
    def _originToSides(self):
        self._sides = NPSides(master = self._master, commands = [lambda event = None: self._sidesToOrigin(), None])
        self._sides.place()
        self._currentPage = "_sides"
        self._origin.place_forget()
    
    def _sidesToOrigin(self):
        self._origin.place()
        self._currentPage = "_origin"
        self._sides.destroy()
        self._sides = None
        
    def _originToA3Price(self):
        self._a3Price = NPA3Price(master = self._master, commands = [lambda event = None: self._priceToOrigin(), lambda event = None: self._a3PriceToA4Price()])
        self._a3Price.place()
        self._currentPage = "_a3Price"
        self._origin.place_forget()
    
    def _a4PriceToA3Price(self):
        self._a3Price.place()
        self._currentPage = "_a3Price"
        self._a4Price.place_forget()
    
    def _a3PriceToA4Price(self):
        if self._a4Price == None:
            self._a4Price = NPA4Price(master = self._master, commands = [lambda event = None: self._a4PriceToA3Price(), lambda event = None: self._a4PriceToA5Price()])
        self._a4Price.place()
        self._currentPage = "_a4Price"
        self._a3Price.place_forget()
    
    def _a5PriceToA4Price(self):
        self._a4Price.place()
        self._currentPage = "_a4Price"
        self._a5Price.place_forget()
    
    def _a4PriceToA5Price(self):
        if self._a5Price == None:
            self._a5Price = NPA5Price(master = self._master, commands = [lambda event = None: self._a5PriceToA4Price(), lambda event = None: self._priceToOrigin()])
        self._a5Price.place()
        self._currentPage = "_a5Price"
        self._a4Price.place_forget()
    
    def _priceToOrigin(self):
        self._origin.place()
        self._currentPage = "_origin"
        attributes = ["_a3Price", "_a4Price", "_a5Price"]
        for attribute in attributes:
            try:
                getattr(self, attribute).destroy()
            except:
                pass
            setattr(self, attribute, None)