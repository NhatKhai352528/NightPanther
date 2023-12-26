from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

currentLanguage = NPLanguage.getLanguage()

class NPWelcome(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None):
        
        super().__init__(master = master, commands = commands)
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = currentLanguage["welcome"]["data"]["title"], wrap = True)
        self._data.initText(mode = "content", text = currentLanguage["welcome"]["data"]["text0"], wrap = True)

        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = currentLanguage["welcome"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = currentLanguage["welcome"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = currentLanguage["welcome"]["interact"]["text0"], justify = "left")
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "content", text = currentLanguage["welcome"]["interact"]["text1"], justify = "left")
        self._interact.initText(mode = "content", text = currentLanguage["welcome"]["interact"]["text2"], justify = "left")
        self._interact.initText(mode = "content", text = currentLanguage["welcome"]["interact"]["text3"], justify = "left")