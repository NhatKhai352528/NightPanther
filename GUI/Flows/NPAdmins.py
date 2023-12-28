from tkinter import Tk
from typing import Any
from ..Pages.Admins.NPAdmin import NPAdmin
from ..Pages.Admins.NPVerify import NPVerify
from ..Pages.Admins.NPError import NPError
from ..Objects.NPConfirmBox import NPConfirmBox
from ..Customs.NPLanguage import NPLanguage 
from time import sleep
import subprocess

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

    def _adminToError(self):
        self._initError()

    def _errorToAdmin(self):
        self._initAdmin()
        attributes = ["_error"]
        for attribute in attributes:
            try:
                getattr(self, attribute).destroy()
            except:
                pass
            setattr(self, attribute, None)
    
    def _displayLog(self):
        subprocess.run(["clear"])
        subprocess.run(["cat", "error_log.txt"])
        self._master.destroy()

    def _markErrorFixed(self):
        empty_file = open("error_log.txt", "w")
        empty_file.close()
        self._master.markErrorFixed()
        self._errorToAdmin()
    
    def _displaySystemState(self):
        if self._master.npget(attribute = "state") == "error":
            NPConfirmBox(master = self._master, messageText = "He thong dang loi", buttonTexts = ["Xem file log", "OK"], buttonCommands = [self._displayLog, None])
        else:
            NPConfirmBox(master = self._master, messageText = "He thong dang hoat dong binh thuong", buttonTexts = [None, "OK"], buttonCommands = [None, None])

    def _initAdmin(self):
        self._admin = NPAdmin(master = self._master, commands = [self._destroyCommand, lambda event = None: self._adminToVerify()], switchCommands = [lambda event = None: self._adminToError(), lambda event = None: NPConfirmBox(master = self._master, messageText = self._currentLanguage["confirmBox"]["message"]["turnOffProgram"], buttonTexts = [self._currentLanguage["confirmBox"]["options"]["remain"], self._currentLanguage["confirmBox"]["options"]["return"]], buttonCommands = [None, lambda event = None: self._master.destroy()])])
        self._admin.place()
    
    def _initVerify(self):
        self._verify = NPVerify(master = self._master, commands = [self._destroyCommand, lambda event = None: self._verifyToAdmin()])
        self._verify.place()

    def _initError(self):
        if (self._master.npget(attribute = "state") == "error"):
            error_file = open("error_log.txt", "r")
            self._error = NPError(master = self._master, commands = [lambda event = None: self._errorToAdmin(), lambda event = None: NPConfirmBox(master = self._master, messageText = "Chac la het loi chua?", buttonTexts = ["Huy", "Het roi"], buttonCommands = [None, lambda event = None: self._markErrorFixed()])], errorList = error_file.read().split('\n'))
            error_file.close()
            self._error.place()
        else:
            NPConfirmBox(master = self._master, messageText = "He thong binh thuong", buttonTexts = [None, "OK"], buttonCommands = [None, None])
        
