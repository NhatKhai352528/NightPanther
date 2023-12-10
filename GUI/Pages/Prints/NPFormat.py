from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

currentLanguage = NPLanguage.getLanguage()

class NPFormat(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None, fileName: str = None, availablePaper: list[bool] = None, availableSides: list[bool] = None):
        
        super().__init__(master)
        
        # Passed commands handler
        self._commands = [Any, Any]
        try:
            self._commands[0] = commands[0]
        except:
            self._commands[0] = None
        try:
            self._commands[1] = commands[1]
        except:
            self._commands[1] = None
        
        # Passed variables handler
        self._fileName = fileName if fileName != None else ""
        
        availablePaper = availablePaper if availablePaper != None else [True, True, True]
        availablePaper = [["default" if value == True else "disabled" for value in availablePaper]]
        for i in range(len(availablePaper)):
            if availablePaper[0][i] == "default":
                availablePaper[0][i] = "active"
                break
        availableSides = availableSides if availableSides != None else [True, True]
        availableSides = [["default" if value == True else "disabled" for value in availableSides]]
        for i in range(len(availableSides)):
            if availableSides[0][i] == "default":
                availableSides[0][i] = "active"
                break
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = currentLanguage["format"]["data"]["title"], wrap = True)
        
        self._data.initText(mode = "heading", text = currentLanguage["format"]["data"]["text0"], wrap = False)
        self._data.initText(mode = "Content", text = self._fileName, wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = currentLanguage["format"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = currentLanguage["format"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = currentLanguage["format"]["interact"]["text0"], justify = "center")
        self._filePaperIndex = self._interact.initButtonArray(mode = "single", rows = 1, columns = 3, defaults = availablePaper, texts=[["A3", "A4", "A5"]])
        self._filePaperButtonArray = self._interact.npget(attribute = "buttonArray", index = self._filePaperIndex)
        
        self._interact.initText(mode = "heading", text = currentLanguage["format"]["interact"]["text1"], justify = "center")
        self._fileSidesIndex = self._interact.initButtonArray(mode = "single", rows = 1, columns = 2, defaults = availableSides, texts=[["1", "2"]])
        self._fileSidesButtonArray = self._interact.npget(attribute = "buttonArray", index = self._fileSidesIndex)
    
    def npset(self, attribute: str, value: Any = None):
        if attribute == "fileName":
            self._fileName = value
            self._data.updateText(index = self._fileNameIndex, text = self._fileName)
    
    def npget(self, attribute: str):
        if attribute == "filePaper":
            if self._filePaperButtonArray.npget("active")[0][0] == True:
                return "a3"
            elif self._filePaperButtonArray.npget("active")[0][1] == True:
                return "a4"
            elif self._filePaperButtonArray.npget("active")[0][2] == True:
                return "a5"
        elif attribute == "fileSides":
            if self._fileSidesButtonArray.npget("active")[0][0]:
                return "1s"
            elif self._fileSidesButtonArray.npget("active")[0][1]:
                return "2s"