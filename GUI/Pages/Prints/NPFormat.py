from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

currentLanguage = NPLanguage.getLanguage()

class NPFormat(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None, fileName: str = None):
        
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
        self._fileName = fileName
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = currentLanguage["format"]["data"]["title"], wrap = True)
        self._data.initText(mode = "heading", text = currentLanguage["format"]["data"]["text0"], wrap = False)
        self._data.initText(mode = "Content", text = self._fileName, wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = currentLanguage["format"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = currentLanguage["format"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "heading", text = currentLanguage["format"]["interact"]["text0"], justify = "center")
        self._interact.initButtonArray(mode = "single", rows = 1, columns = 3, defaults=None, texts=[["A3", "A4", "A5"]])
        self._interact.initText(mode = "heading", text = currentLanguage["format"]["interact"]["text1"], justify = "center")
        self._interact.initButtonArray(mode = "single", rows = 1, columns = 2, defaults=None, texts=[["1", "2"]])