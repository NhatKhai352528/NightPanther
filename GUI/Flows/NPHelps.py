from tkinter import Tk
from typing import Any, Literal, Optional
from ..Pages.Helps.NPError import NPError
from ..Pages.Helps.NPInitial import NPInitial
from ..Pages.Helps.NPPay import NPPay
from ..Pages.Helps.NPPrint import NPPrint
from ..Pages.Helps.NPUpload import NPUpload

class NPHelps:
    
    def __init__(self, master: Tk, destroyCommand: Any):
    
        self._master = master
        self._destroyCommand = destroyCommand
        
        # Pages
        self._initial = None
        self._upload = None
        self._print = None
        self._pay = None
        self._error = None
        
        self._pages = Literal["_initial", "_upload", "_print", "_pay", "_error"]
        self._currentPage: Optional[self._pages] = None
        
    def place(self):
        if self._currentPage == None:
            self._initInitial()
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
    
    def _initInitial(self):
        self._initial = NPInitial(master = self._master, commands = [self._destroyCommand, None], switchCommands = [lambda event = None: self._initialToUpload(), lambda event = None: self._initialToPrint(), lambda event = None: self._initialToPay(), lambda event = None: self._initialToError(), None])
        self._initial.place()
        self._currentPage = "_initial"
    
    def _initialToUpload(self):
        self._upload = NPUpload(master = self._master, commands = [lambda event = None: self._uploadToInitial(), None])
        self._upload.place()
        self._currentPage = "_upload"
        self._initial.place_forget()
    
    def _uploadToInitial(self):
        self._initial.place()
        self._currentPage = "_initial"
        self._upload.destroy()
        self._upload = None

    def _initialToPrint(self):
        self._print = NPPrint(master = self._master, commands = [lambda event = None: self._printToInitial(), None])
        self._print.place()
        self._currentPage = "_print"
        self._initial.place_forget()
    
    def _printToInitial(self):
        self._initial.place()
        self._currentPage = "_initial"
        self._print.destroy()
        self._print = None
    
    def _initialToPay(self):
        self._pay = NPPay(master = self._master, commands = [lambda event = None: self._payToInitial(), None])
        self._pay.place()
        self._currentPage = "_pay"
        self._initial.place_forget()
    
    def _payToInitial(self):
        self._initial.place()
        self._currentPage = "_initial"
        self._pay.destroy()
        self._pay = None
    
    def _initialToError(self):
        self._error = NPError(master = self._master, commands = [lambda event = None: self._errorToInitial(), None])
        self._error.place()
        self._currentPage = "_error"
        self._initial.place_forget()
    
    def _errorToInitial(self):
        self._initial.place()
        self._currentPage = "_initial"
        self._error.destroy()
        self._error = None