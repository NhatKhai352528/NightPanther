from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

currentLanguage = NPLanguage.getLanguage()

class NPPrinting(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None, fileName: str = None, filePages: int = None, userCopies: int = None):
        
        super().__init__(master = master, commands = commands)
        
        # Passed variables handler
        self._fileName = fileName if fileName != None else ""
        self._filePages = filePages if filePages != None else 0
        self._userCopies = userCopies if userCopies != None else 0
        self._printerPage = 0
        self._printerCopy = 0
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = currentLanguage["printing"]["data"]["title"], wrap = True)
        # self._data.initText(mode = "Content", text = currentLanguage["printing"]["data"]["text0"], wrap = False)
        
        self._data.initText(mode = "heading", text = currentLanguage["printing"]["data"]["text1"], wrap = False)
        self._fileNameIndex = self._data.initText(mode = "content", text = self._fileName, wrap = False)
        
        # Initialize items for control frame
        # self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = currentLanguage["printing"]["control"]["cancel"])
        # self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = currentLanguage["printing"]["control"]["pause"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = currentLanguage["printing"]["interact"]["text0"], justify = "center")
        self._interact.initText(mode = "content", text = "", justify = "center")
        
        self._userProgressIndex = self._interact.initProgressBar(default = 0, maximum = self._filePages * self._userCopies)
        self._userProgressProgressBar = self._interact.npget(attribute = "progressBar", index = self._userProgressIndex)
        
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._printerPageIndex = self._interact.initText(mode = "content", text = currentLanguage["printing"]["interact"]["text1"] + str(self._printerPage) + "/" + str(self._filePages), justify = "center")
        
        self._printerCopyIndex = self._interact.initText(mode = "content", text = currentLanguage["printing"]["interact"]["text2"] + str(self._printerCopy) + "/" + str(self._userCopies), justify = "center")
    
    def npset(self, attribute: str, value: Any = None):
        if attribute == "fileName":
            self._fileName = value
            self._data.updateText(index = self._fileNameIndex, text = self._fileName)
        elif attribute == "filePages":
            self._filePages = value
            self._userProgressProgressBar.npset(attribute = "maximum", value = self._filePages * self._userCopies)
            self._interact.updateText(index = self._printerPageIndex, text = currentLanguage["printing"]["interact"]["text1"] + str(self._printerPage) + "/" + str(self._filePages))
        elif attribute == "userCopies":
            self._userCopies = value
            self._userProgressProgressBar.npset(attribute = "maximum", value = self._filePages * self._userCopies)
            self._interact.updateText(index = self._printerCopyIndex, text = currentLanguage["printing"]["interact"]["text2"] + str(self._printerCopy) + "/" + str(self._userCopies))
        elif attribute == "printerPage":
            self._printerPage = value
            self._userProgressProgressBar.npset(attribute = "value", value = self._filePages * self._printerCopy + self._printerPage % self._filePages)
            self._interact.updateText(index = self._printerPageIndex, text = currentLanguage["printing"]["interact"]["text1"] + str(self._printerPage) + "/" + str(self._filePages))
        elif attribute == "printerCopy":
            self._printerCopy = value
            self._userProgressProgressBar.npset(attribute = "value", value = self._filePages * self._printerCopy + self._printerPage % self._filePages)
            self._interact.updateText(index = self._printerCopyIndex, text = currentLanguage["printing"]["interact"]["text2"] + str(self._printerCopy) + "/" + str(self._userCopies))
        
    def npget(self, attribute: str):
        if attribute == "printerPage":
            return self._printerPage
        elif attribute == "printerCopy":
            return self._printerCopy
            