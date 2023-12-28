from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

class NPVerify(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any] = None):

        self._currentLanguage = NPLanguage.getLanguage()
        
        super().__init__(master = master, commands = commands)
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = self._currentLanguage["adminVerify"]["data"]["title"], wrap = True)
        self._data.initText(mode = "content", text = "", wrap = False)
        self._modeIndex = self._data.initText(mode = "content", text = self._currentLanguage["adminVerify"]["data"]["loggedOut"] if self._master.npget(attribute = "mode") == "user" else self._currentLanguage["adminVerify"]["data"]["loggedIn"], wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = self._currentLanguage["adminVerify"]["control"]["back"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = self._currentLanguage["adminVerify"]["control"]["logIn"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "heading", text = self._currentLanguage["adminVerify"]["interact"]["text0"], justify = "center")
        self._passwordIndex = self._interact.initKeyBoard(default = "", maximum = 8, show = "*", inputTexts = None, actionTexts = None, actionCommands = None)
        self._passwordKeyBoard = self._interact.npget(attribute = "keyBoard", index = self._passwordIndex)
    
    def npget(self, attribute: str):
        if attribute == "password":
            return self._passwordKeyBoard.npget(attribute = "value")
