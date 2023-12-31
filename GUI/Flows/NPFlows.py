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
from ..Customs.NPLanguage import NPLanguage

class NPFlows:
    
    def __init__(self, master: Tk):
        
        self._currentLanguage = NPLanguage.getLanguage()
        
        self._master = master
        self._bars = None
        
        # Flows
        self._starts = None
        self._setups = None
        self._prints = None
        self._helps = None
        self._settings = None
        self._admins = None
        
        self._mainFlows = Literal["_setups", "_prints"]
        self._subFlows = Literal["_helps", "_settings", "_admins"]
        self._flows = Literal["_bars", "_starts", "_setups", "_prints", "_helps", "_settings", "_admins"]
        
        self._previousFlow: Optional[Literal["_start", Union[self._mainFlows, self._subFlows]]] = None
        self._currentFlow: Optional[Literal["_start", Union[self._mainFlows, self._subFlows]]] = None
    
    def place(self):
        self._bars = NPBars(master = self._master, menuCommands = [lambda event = None: self._confirmToStart(), lambda event = None: self._currentToHelps(), lambda event = None: self._currentToSettings(), lambda event = None: self._currentToAdmins()])
        self._bars.place()
        self._currentToStarts()
    
    def destroy(self):
        for flow in self._flows.__args__:
            try:
                getattr(self, flow).destroy()
            except:
                pass
        self.__dict__.clear()
    
    #
    # Starts
    
    def _confirmToStart(self):
        if self._currentFlow == "_starts":
            return
        NPConfirmBox(master = self._master, messageText = self._currentLanguage["popup"]["confirm"]["reset"], buttonTexts = [self._currentLanguage["popup"]["options"]["remain"], self._currentLanguage["popup"]["options"]["return"]], buttonCommands = [None, lambda event = None: self._currentToStarts()])
    
    def _currentToStarts(self):
        
        if self._currentFlow != "_starts":
            self._starts = NPStarts(master = self._master, controlCommands = [lambda event = None: self._startsToSetups(), lambda event = None: self._startsToPrints()])
            self._starts.place()
            self._currentFlow = "_starts"
        
        # Automatically destroy unusable flows
        for flow in self._mainFlows.__args__ + self._subFlows.__args__:
            try:
                getattr(self, flow).destroy()
            except:
                pass
            setattr(self, flow, None)
    
    #
    # Helps
    
    def _currentToHelps(self):
        if self._currentFlow == "_helps":
            return
        if self._currentFlow in self._subFlows.__args__:
            NPConfirmBox(master = self._master, messageText = self._currentLanguage["popup"]["guide"]["goToHelpFromAny"], buttonTexts = [None, "OK"], buttonCommands = [None, None])
            return
        if self._currentFlow != "_helps":
            self._helps = NPHelps(master = self._master, destroyCommand = lambda event = None: self._helpsToPrevious())
            self._previousFlow = self._currentFlow
            self._helps.place()
            self._currentFlow = "_helps"
            getattr(self, self._previousFlow).place_forget()
    
    def _helpsToPrevious(self):
        if self._currentFlow == "_helps":
            getattr(self, self._previousFlow).place()
            self._currentFlow = self._previousFlow
            self._helps.destroy()
            self._helps = None
    
    #
    # Settings
    
    def _currentToSettings(self):
        if self._currentFlow == "_settings":
            return
        if self._currentFlow in self._subFlows.__args__:
            NPConfirmBox(master = self._master, messageText = self._currentLanguage["popup"]["guide"]["goToSettingFromSubflow"], buttonTexts = [None, "OK"], buttonCommands = [None, None])
            return
        if self._currentFlow != "_settings":
            self._settings = NPSettings(master = self._master, destroyCommand = lambda event = None: self._settingsToPrevious())
            self._previousFlow = self._currentFlow
            self._settings.place()
            self._currentFlow = "_settings"
            getattr(self, self._previousFlow).place_forget()
    
    def _settingsToPrevious(self):
        if self._currentFlow == "_settings":
            getattr(self, self._previousFlow).place()
            self._currentFlow = self._previousFlow
            self._settings.destroy()
            self._settings = None
    
    #
    # Admins
    
    def _currentToAdmins(self):
        if self._currentFlow == "_admins":
            return
        if self._currentFlow in self._subFlows.__args__:
            NPConfirmBox(master = self._master, messageText = self._currentLanguage["popup"]["guide"]["goToAdminFromAny"], buttonTexts = [None, "OK"], buttonCommands = [None, None])
            return
        if self._currentFlow != "_admins":
            self._admins = NPAdmins(master = self._master, destroyCommand = lambda event = None: self._adminsToPrevious())
            self._previousFlow = self._currentFlow
            self._admins.place()
            self._currentFlow = "_admins"
            getattr(self, self._previousFlow).place_forget()
    
    def _adminsToPrevious(self):
        if self._currentFlow == "_admins":
            getattr(self, self._previousFlow).place()
            self._currentFlow = self._previousFlow
            self._admins.destroy()
            self._admins = None
    
    #
    # Prints
    
    def _startsToPrints(self):
        if self._currentFlow == "_starts":
            if self._master.npget(attribute = "state") == "error" and self._master.npget(attribute = "mode") != "admin":
                NPConfirmBox(master = self._master, messageText = self._currentLanguage["popup"]["error"]["systemError"], buttonTexts = [None, "OK"], buttonCommands = [None, None])
                return
            self._prints = NPPrints(master = self._master, destroyCommand = lambda event = None: self._currentToStarts())
            self._prints.place()
            self._currentFlow = "_prints"
            self._starts.destroy()
            self._starts = None
    
    #
    # Setups
    
    def _startsToSetups(self):
        if self._master.npget(attribute = "mode") != "admin":
            NPConfirmBox(master = self._master, messageText = self._currentLanguage["popup"]["guide"]["goToSetupNotLoggedIn"], buttonTexts = [None, "OK"], buttonCommands = [None, None])
            return
        if self._currentFlow == "_starts":
            self._setups = NPSetups(master = self._master, destroyCommand = lambda event = None: self._currentToStarts())
            self._setups.place()
            self._currentFlow = "_setups"
            self._starts.destroy()
            self._starts = None
