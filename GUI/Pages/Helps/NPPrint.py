from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

class NPPrint(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None):

        self._currentLanguage = NPLanguage.getLanguage()
        
        super().__init__(master = master, commands = commands)
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = self._currentLanguage["helpPrint"]["data"]["title"], wrap = True)
        self._data.initText(mode = "content", text = self._currentLanguage["helpPrint"]["data"]["text0"], wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = self._currentLanguage["helpPrint"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = self._currentLanguage["helpPrint"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = self._currentLanguage["helpPrint"]["interact"]["text0"], justify = "left")
        self._interact.initText(mode = "content", text = self._currentLanguage["helpPrint"]["interact"]["text1"], justify = "left")
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = self._currentLanguage["helpPrint"]["interact"]["text2"], justify = "left")
        self._interact.initText(mode = "content", text = self._currentLanguage["helpPrint"]["interact"]["text3"], justify = "left")
