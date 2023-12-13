from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Constants.NPPaper import Paper
from ...Customs.NPLanguage import NPLanguage

currentLanguage = NPLanguage.getLanguage()

class NPPaper(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None):
        
        super().__init__(master = master, commands = commands)
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = currentLanguage["paper"]["data"]["title"], wrap = True)
        self._data.initText(mode = "Content", text = currentLanguage["paper"]["data"]["text0"], wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = currentLanguage["paper"]["control"]["left"])
        self._control.initButton(position = "right", command = lambda event = None: self._saveAvailablePaper(), state = "normal", text = currentLanguage["paper"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = currentLanguage["paper"]["interact"]["text0"], justify = "center")
        
        availablePaper = [["active" if value else "default" for value in Paper.values()]]
        
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._availablePaperIndex = self._interact.initButtonArray(mode = "multiple", rows = 1, columns = 3, defaults = availablePaper, texts = [["A3", "A4", "A5"]])
        self._availablePaperButtonArray = self._interact.npget(attribute = "buttonArray", index = self._availablePaperIndex)

    def _saveAvailablePaper(self):
        currentActive = self._availablePaperButtonArray.npget(attribute = "active")
        for (paper, active) in zip(Paper.keys(), currentActive[0]):
            Paper[paper] = active
        self._currentActive = currentActive
        with open("GUI/Constants/NPPaper.py", "w") as file:
            file.write("Paper = " + repr(Paper))
