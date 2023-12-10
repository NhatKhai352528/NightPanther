from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

currentLanguage = NPLanguage.getLanguage()

class NPSuccess(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None):
        
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
        
        # Initialize items for data frame
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._data.initText(mode = "title", text = currentLanguage["success"]["data"]["title"], wrap = True)
        self._data.initText(mode = "Content", text = currentLanguage["success"]["data"]["text0"], wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = currentLanguage["success"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = currentLanguage["success"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "heading", text = currentLanguage["success"]["interact"]["text0"], justify = "center")
        self._interact.initText(mode = "content", text = currentLanguage["success"]["interact"]["text1"], justify = "center")