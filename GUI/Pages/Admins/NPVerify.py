from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

currentLanguage = NPLanguage.getLanguage()

class NPVerify(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any] = None):
        
        super().__init__(master = master, commands = commands)
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = currentLanguage["error"]["data"]["title"], wrap = True)
        self._data.initText(mode = "Content", text = currentLanguage["error"]["data"]["text0"], wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = currentLanguage["error"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = currentLanguage["error"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "heading", text = currentLanguage["error"]["interact"]["text0"], justify = "center")
        
        self._keyBoardTexts = ["Yoo", "Yaa"]
        self._keyBoardCommands = [lambda event = None: self._master.signOut(), lambda event = None: self._master.signIn(password = self._passwordKeyBoard.npget(attribute = "value"))]
        self._passwordIndex = self._interact.initKeyBoard(default = "", maximum = 8, show = "*", inputTexts = None, actionTexts = self._keyBoardTexts, actionCommands = self._keyBoardCommands)
        self._passwordKeyBoard = self._interact.npget(attribute = "keyBoard", index = self._passwordIndex)
