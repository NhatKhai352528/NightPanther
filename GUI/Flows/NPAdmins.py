from tkinter import Tk
from typing import Any, Literal, Optional, Union
from ..Pages.Admins.NPAdmin import NPAdmin
from ..Pages.Admins.NPError import NPError
from ..Pages.Admins.NPTutorial1 import NPTutorial1
from ..Pages.Admins.NPTutorial2 import NPTutorial2
from ..Pages.Admins.NPTutorial3 import NPTutorial3
from ..Pages.Admins.NPVerify import NPVerify
from ..Objects.NPConfirmBox import NPConfirmBox
from ..Customs.NPLanguage import NPLanguage

class NPAdmins:
    
    def __init__(self, master: Tk, destroyCommand: Any):
        
        self._currentLanguage = NPLanguage.getLanguage()

        self._master = master
        self._destroyCommand = destroyCommand
        
        # Pages
        self._admin = None
        self._verify = None
        self._error = None
        self._tutorial1 = None
        self._tutorial2 = None
        self._tutorial3 = None
        
        self._userPages = Literal["_verify"]
        self._tutorialPages = Literal["_tutorial1", "_tutorial2", "_tutorial3"]
        self._adminPages = Literal["_admin", "_error", "_tutorial1", "_tutorial2", "_tutorial3"]
                
        self._pages = Literal["_verify", "_admin", "_error", "_tutorial1", "_tutorial2", "_tutorial3"]
        self._currentPage: Optional[self._pages] = None
        
    def place(self):
        if self._currentPage == None:
            if self._master.npget(attribute = "mode") == "user":
                self._initVerify()
            elif self._master.npget(attribute = "mode") == "admin":
                self._initAdmin()
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
    
    def _verifyToAdmin(self):
        self._master.signIn(password = self._verify.npget(attribute = "password"))
        if self._master.npget(attribute = "mode") == "user":
            NPConfirmBox(master = self._master, messageText = self._currentLanguage["popup"]["error"]["incorrectPassword"], buttonTexts = [None, "OK"], buttonCommands = [None, None])
        elif self._master.npget(attribute = "mode") == "admin":
            self._initAdmin()
            for page in self._userPages.__args__:
                try:
                    getattr(self, page).destroy()
                except:
                    pass
                setattr(self, page, None)
    
    def _adminToVerify(self):
        self._master.signOut()
        if self._master.npget(attribute = "mode") == "user":
            self._initVerify()
            for page in self._adminPages.__args__:
                try:
                    getattr(self, page).destroy()
                except:
                    pass
                setattr(self, page, None)

    def _adminToError(self):
        if (self._master.npget(attribute = "state") == "error"):
            error_file = open("error_log.txt", "r", encoding = "utf8")
            self._error = NPError(master = self._master, commands = [lambda event = None: self._errorToAdmin(), lambda event = None: NPConfirmBox(master = self._master, messageText = self._currentLanguage["popup"]["confirm"]["completeDebug"], buttonTexts = [self._currentLanguage["popup"]["options"]["no"], self._currentLanguage["popup"]["options"]["yes"]], buttonCommands = [None, lambda event = None: self._markErrorFixed()])], errorList = error_file.read().split('\n'))
            error_file.close()
            self._error.place()
            self._currentPage = "_error"
            self._admin.place_forget()
        else:
            NPConfirmBox(master = self._master, messageText = self._currentLanguage["popup"]["guide"]["noError"], buttonTexts = [None, "OK"], buttonCommands = [None, None])

    def _errorToAdmin(self):
        self._admin.place()
        self._currentPage = "_admin"
        self._error.destroy()
        self._error = None
    
    def _adminToTutorial1(self):
        self._tutorial1 = NPTutorial1(master = self._master, commands = [lambda event = None: self._tutorialToAdmin(), lambda event = None: self._tutorial1ToTutorial2()])
        self._tutorial1.place()
        self._currentPage = "_tutorial1"
        self._admin.place_forget()
    
    def _tutorial1ToTutorial2(self):
        if self._tutorial2 == None:
            self._tutorial2 = NPTutorial2(master = self._master, commands = [lambda event = None: self._tutorial2ToTutorial1(), lambda event = None: self._tutorial2ToTutorial3()])
        self._tutorial2.place()
        self._currentPage = "_tutorial2"
        self._tutorial1.place_forget()
    
    def _tutorial2ToTutorial1(self):
        self._tutorial1.place()
        self._currentPage = "_tutorial1"
        self._tutorial2.place_forget()
    
    def _tutorial2ToTutorial3(self):
        if self._tutorial3 == None:
            self._tutorial3 = NPTutorial3(master = self._master, commands = [lambda event = None: self._tutorial3ToTutorial2(), lambda event = None: self._tutorialToAdmin()])
        self._tutorial3.place()
        self._currentPage = "_tutorial3"
        self._tutorial2.place_forget()
    
    def _tutorial3ToTutorial2(self):
        self._tutorial2.place()
        self._currentPage = "_tutorial2"
        self._tutorial3.place_forget()
    
    def _tutorialToAdmin(self):
        self._admin.place()
        self._currentPage = "_admin"
        for page in self._tutorialPages.__args__:
            try:
                getattr(self, page).destroy()
            except:
                pass
            setattr(self, page, None)

    def _markErrorFixed(self):
        empty_file = open("error_log.txt", "w", encoding = "utf8")
        empty_file.close()
        self._master.markErrorFixed()
        self._errorToAdmin()

    def _initAdmin(self):
        self._admin = NPAdmin(master = self._master, commands = [self._destroyCommand, lambda event = None: self._adminToVerify()], switchCommands = [lambda event = None: self._adminToTutorial1(), lambda event = None: self._adminToError(), None, lambda event = None: NPConfirmBox(master = self._master, messageText = self._currentLanguage["popup"]["confirm"]["turnOffProgram"], buttonTexts = [self._currentLanguage["popup"]["options"]["remain"], self._currentLanguage["popup"]["options"]["return"]], buttonCommands = [None, lambda event = None: self._master.destroy()])])
        self._admin.place()
        self._currentPage = "_admin"
    
    def _initVerify(self):
        self._verify = NPVerify(master = self._master, commands = [self._destroyCommand, lambda event = None: self._verifyToAdmin()])
        self._verify.place()
        self._currentPage = "_verify"
