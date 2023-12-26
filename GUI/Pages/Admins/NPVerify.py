from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

class NPVerify(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any] = None):

        self._currentLanguage = NPLanguage.getLanguage()
        
        super().__init__(master = master, commands = commands)
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = self._currentLanguage["admin"]["data"]["title"], wrap = True)
        self._data.initText(mode = "content", text = "", wrap = False)
        self._modeIndex = self._data.initText(mode = "content", text = self._currentLanguage["admin"]["data"]["loggedOut"] if self._master.npget(attribute = "mode") == "user" else self._currentLanguage["admin"]["data"]["loggedIn"], wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = self._currentLanguage["admin"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = self._currentLanguage["admin"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "heading", text = self._currentLanguage["admin"]["interact"]["text0"], justify = "center")
        
        self._keyBoardTexts = ["Log Out", "Log In"]
        self._keyBoardCommands = [lambda event = None: (self._master.signOut(), self.npset(attribute = "mode", value = None)), lambda event = None: (self._master.signIn(password = self._passwordKeyBoard.npget(attribute = "value")), self.npset(attribute = "mode", value = None))]
        self._passwordIndex = self._interact.initKeyBoard(default = "", maximum = 8, show = "*", inputTexts = None, actionTexts = self._keyBoardTexts, actionCommands = self._keyBoardCommands)
        self._passwordKeyBoard = self._interact.npget(attribute = "keyBoard", index = self._passwordIndex)
    
    def npset(self, attribute: str, value: Any = None):
        if attribute == "mode":
            self._data.updateText(index = self._modeIndex, text = self._currentLanguage["admin"]["data"]["loggedOut"] if self._master.npget(attribute = "mode") == "user" else self._currentLanguage["admin"]["data"]["loggedIn"])
