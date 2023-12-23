from tkinter import Tk
from typing import Literal, Optional, Union
from .NPAdmins import NPAdmins
from .NPBars import NPBars
from .NPHelps import NPHelps
from .NPPrints import NPPrints
from .NPSettings import NPSettings
from .NPSetups import NPSetups
from .NPStarts import NPStarts
from ..Objects.NPConfirmBox import NPConfirmBox
import globals
import socket
from threading import Thread
from ..Customs.NPLanguage import NPLanguage
from ..Customs.NPTheme import NPTheme

currentLanguage = NPLanguage.getLanguage()
currentTheme = NPTheme.getTheme()

class NPFlows:
    
    def __init__(self, master: Tk):
        
        self._master = master
        self._bars = None
        
        # Flows
        self._starts = None
        self._setups = None
        self._prints = None
        self._helps = None
        self._settings = None
        self._admins = None
        
        self._mainFlow = Literal["starts", "setups", "prints"]
        self._subFlow = Literal["helps", "settings", "admins"]
        self._previousFlow: Optional[Union[self._mainFlow, self._subFlow]] = None
        self._currentFlow: Optional[Union[self._mainFlow, self._subFlow]] = None
    
    def place(self):
        self._bars = NPBars(master = self._master, menuCommands = [lambda event = None: self._currentToStarts(), lambda event = None: self._currentToHelps(), lambda event = None: self._currentToSettings(), lambda event = None: self._currentToAdmins()])
        self._bars.place()
        self._currentToStarts()
        startConnection = Thread(target = self._startConnection)
        startConnection.start()
    
    def destroy(self):
        attributes = ["_bars", "_starts", "_setups", "_prints", "_helps", "_settings", "_admins"]
        for attribute in attributes:
            try:
                getattr(self, attribute).destroy()
            except:
                pass
        self.__dict__.clear()
    
    #
    # Starts
    
    def _currentToStarts(self):
        
        if self._currentFlow != "starts":
            self._currentFlow = "starts"
            self._starts = NPStarts(master = self._master, controlCommands = [lambda event = None: self._startsToSetups(), lambda event = None: self._startsToPrints()])
            self._starts.place()
        
        # Automatically destroy unusable flows
        attributes = ["_setups", "_prints", "_helps", "_settings", "_admins"]
        for attribute in attributes:
            try:
                getattr(self, attribute).destroy()
            except:
                pass
            setattr(self, attribute, None)
    
    #
    # Helps
    
    def _currentToHelps(self):
        if self._currentFlow in self._subFlow.__args__:
            NPConfirmBox(master = self._master, messageText = "Please go back first!", buttonTexts = [None, None, "OK"], buttonCommands = [None, None, None])
            return
        if self._currentFlow != "helps":
            self._previousFlow = self._currentFlow
            self._currentFlow = "helps"
            self._helps = NPHelps(master = self._master, destroyCommand = lambda event = None: self._helpsToPrevious())
            self._helps.place()
    
    def _helpsToPrevious(self):
        if self._currentFlow == "helps":
            self._currentFlow = self._previousFlow
            self._helps.destroy()
            self._helps = None
    
    #
    # Settings
    
    def _currentToSettings(self):
        if self._currentFlow in self._subFlow.__args__:
            NPConfirmBox(master = self._master, messageText = "Hha kitchen", buttonTexts = [None, None, "Kayy"], buttonCommands = [None, None, None])
            return
        if self._master.npget(attribute = "mode") != "admin":
            NPConfirmBox(master = self._master, messageText = "Hehe kitchen", buttonTexts = [None, None, "Kayy"], buttonCommands = [None, None, None])
            return
        if self._currentFlow != "settings":
            self._previousFlow = self._currentFlow
            self._currentFlow = "settings"
            self._settings = NPSettings(master = self._master, destroyCommand = lambda event = None: self._settingsToPrevious())
            self._settings.place()
    
    def _settingsToPrevious(self):
        if self._currentFlow == "settings":
            self._currentFlow = self._previousFlow
            self._settings.destroy()
            self._settings = None
    
    #
    # Admins
    
    def _currentToAdmins(self):
        if self._currentFlow in self._subFlow.__args__:
            NPConfirmBox(master = self._master, messageText = "Hha kitchen", buttonTexts = [None, None, "Kayy"], buttonCommands = [None, None, None])
            return
        if self._currentFlow != "admins":
            self._previousFlow = self._currentFlow
            self._currentFlow = "admins"
            self._admins = NPAdmins(master = self._master, destroyCommand = lambda event = None: self._adminsToPrevious())
            self._admins.place()
    
    def _adminsToPrevious(self):
        if self._currentFlow == "admins":
            self._currentFlow = self._previousFlow
            self._admins.destroy()
            self._admins = None
    
    #
    # Prints
    
    def _startsToPrints(self):
        if self._currentFlow == "starts":
            self._currentFlow = "prints"
            self._prints = NPPrints(master = self._master, destroyCommand = lambda event = None: self._currentToStarts())
            self._prints.place()
            self._starts.destroy()
            self._starts = None
    
    #
    # Setups
    
    def _startsToSetups(self):
        if self._master.npget(attribute = "mode") != "admin":
            NPConfirmBox(master = self._master, messageText = "Hihi kitchen", buttonTexts = [None, None, "Kayy"], buttonCommands = [None, None, None])
            return
        if self._currentFlow == "starts":
            self._currentFlow = "setups"
            self._setups = NPSetups(master = self._master, destroyCommand = lambda event = None: self._currentToStarts())
            self._setups.place()
            self._starts.destroy()
            self._starts = None

    #
    # Start connection to Local web server
    def _startConnection(self):
        globals.ipcPort = 2020
        globals.ipcSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        globals.ipcSocket.bind(('', globals.ipcPort))
        globals.ipcSocket.listen(100)
        (globals.webServerSocket, _) = globals.ipcSocket.accept()