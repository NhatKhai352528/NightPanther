from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Constants.NPPaper import Paper
from ...Constants.NPSides import Sides
from ...Customs.NPLanguage import NPLanguage

currentLanguage = NPLanguage.getLanguage()

class NPFormat(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None, fileName: str = None, availablePaper: list[bool] = None, availableSides: list[bool] = None):
        
        super().__init__(master = master, commands = commands)
        
        # Passed variables handler
        self._fileName = fileName if fileName != None else ""
        
        availablePaper = [["default" if value else "disabled" for value in Paper.values()]]
        for i in range(len(availablePaper[0])):
            if availablePaper[0][i] == "default":
                availablePaper[0][i] = "active"
                break
        
        availableSides =  [["default" if value else "disabled" for value in Sides.values()]]
        for i in range(len(availableSides[0])):
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
            if self._filePaperButtonArray.npget(attribute = "active")[0][0] == True:
                return "a3"
            elif self._filePaperButtonArray.npget(attribute = "active")[0][1] == True:
                return "a4"
            elif self._filePaperButtonArray.npget(attribute = "active")[0][2] == True:
                return "a5"
        elif attribute == "fileSides":
            if self._fileSidesButtonArray.npget(attribute = "active")[0][0]:
                return "1s"
            elif self._fileSidesButtonArray.npget(attribute = "active")[0][1]:
                return "2s"