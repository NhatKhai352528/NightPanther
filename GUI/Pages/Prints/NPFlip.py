from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

class NPFlip(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None, fileLayout: str = None):

        self._currentLanguage = NPLanguage.getLanguage()
        self._fileLayout = fileLayout

        super().__init__(master = master, commands = commands)
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = self._currentLanguage["welcome"]["data"]["title"], wrap = True)
        self._data.initText(mode = "content", text = self._currentLanguage["welcome"]["data"]["text0"], wrap = True)

        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = self._currentLanguage["welcome"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = self._currentLanguage["welcome"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = self._currentLanguage["welcome"]["interact"]["text0"], justify = "left")
        self._interact.initText(mode = "content", text = "", justify = "center")
       
        self._fileLayoutIndex = self._interact.initButtonSet(mode = "single", rows = 1, columns = 2, defaults = [["default", "active"]], imageFiles = [[None, None]])
        self._fileLayoutButtonSet = self._interact.npget(attribute = "buttonSet", index = self._fileLayoutIndex)
        self.npset(attribute = "fileLayout", value = self._fileLayout)
                
    def npset(self, attribute: str, value: Any = None):
        if attribute == "fileLayout":
            self._fileLayout = value
            if self._fileLayout == "portrait":
                self._fileLayoutButtonSet.npset(attribute = "imageFile", value = [0, 0, "./GUI/Images/Home.png"])
                self._fileLayoutButtonSet.npset(attribute = "imageFile", value = [0, 1, "./GUI/Images/Help.png"])
            elif self._fileLayout == "landscape":
                self._fileLayoutButtonSet.npset(attribute = "imageFile", value = [0, 0, "./GUI/Images/Help.png"])
                self._fileLayoutButtonSet.npset(attribute = "imageFile", value = [0, 1, "./GUI/Images/Home.png"])
    
    def npget(self, attribute: str):
        if attribute == "fileLayout":
            return self._fileLayout
        elif attribute == "fileFlip":
            if self._fileLayoutButtonSet.npget(attribute = "active")[0][0] == True:
                return "short-edge"
            elif self._fileLayoutButtonSet.npget(attribute = "active")[0][1] == True:
                return "long-edge"

