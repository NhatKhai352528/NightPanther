from tkinter import Tk
from typing import Any
from ..Pages.Admins.NPAdmin import NPAdmin
from ..Pages.Admins.NPVerify import NPVerify
from ..Objects.NPConfirmBox import NPConfirmBox
from ..Customs.NPLanguage import NPLanguage 
from time import sleep

class NPAdmins:
    
    def __init__(self, master: Tk, destroyCommand: Any):
        self._currentLanguage = NPLanguage.getLanguage()

        self._master = master
        self._destroyCommand = destroyCommand
        
        # Pages
        self._admin = None
        self._verify = None
        
    def place(self):
        if self._master.npget(attribute = "mode") == "user":
            self._initVerify()
        elif self._master.npget(attribute = "mode") == "admin":
            self._initAdmin()
    
    def destroy(self):
        attributes = ["_admin", "_verify"]
        for attribute in attributes:
            try:
                getattr(self, attribute).destroy()
            except:
                pass
        self.__dict__.clear()
    
    def _verifyToAdmin(self):
        self._master.signIn(password = self._verify.npget(attribute = "password"))
        sleep(0.5)
        if self._master.npget(attribute = "mode") == "user":
            NPConfirmBox(master = self._master, messageText = self._currentLanguage["confirmBox"]["message"]["wrongPassword"], buttonTexts = [None, "OK"], buttonCommands = [None, None])
        elif self._master.npget(attribute = "mode") == "admin":
            self._initAdmin()
            attributes = ["_verify"]
            for attribute in attributes:
                try:
                    getattr(self, attribute).destroy()
                except:
                    pass
                setattr(self, attribute, None)
    
    def _adminToVerify(self):
        self._master.signOut()
        sleep(0.5)
        if self._master.npget(attribute = "mode") == "user":
            self._initVerify()
            attributes = ["_admin"]
            for attribute in attributes:
                try:
                    getattr(self, attribute).destroy()
                except:
                    pass
                setattr(self, attribute, None)
    
    def _initAdmin(self):
        # Turn off program
        self._admin = NPAdmin(master = self._master, commands = [self._destroyCommand, lambda event = None: self._adminToVerify()], switchCommands = [None, None, None, lambda event = None: NPConfirmBox(master = self._master, messageText = self._currentLanguage["confirmBox"]["message"]["turnOffProgram"], buttonTexts = [self._currentLanguage["confirmBox"]["options"]["remain"], self._currentLanguage["confirmBox"]["options"]["return"]], buttonCommands = [None, lambda event = None: self._master.destroy()])])
        self._admin.place()
    
    def _initVerify(self):
        self._verify = NPVerify(master = self._master, commands = [self._destroyCommand, lambda event = None: self._verifyToAdmin()])
        self._verify.place()
        