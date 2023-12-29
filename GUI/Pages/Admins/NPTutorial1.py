from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

class NPTutorial1(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None):

        self._currentLanguage = NPLanguage.getLanguage()
        
        super().__init__(master = master, commands = commands)
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = self._currentLanguage["adminInstruction"]["data"]["title"], wrap = True)
        # self._data.initText(mode = "Content", text = self._currentLanguage["adminInstruction"]["data"]["subtitle"], wrap = True)
        self._data.initText(mode = "footnote", text = "", wrap = False)
        self._data.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["data"]["text1"], wrap = True)
        self._data.initText(mode = "footnote", text = "", wrap = False)
        self._data.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["data"]["text2"], wrap = True)

        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = self._currentLanguage["adminInstruction"]["control"]["back"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = self._currentLanguage["adminInstruction"]["control"]["more"])
        
        # Initialize items for interact frame

        # Error unknown
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "contentBold", text = self._currentLanguage["errorLog"]["message"]["errorUnknown"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["interact"]["errorUnknown"]["text0"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["interact"]["errorUnknown"]["text1"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["interact"]["errorUnknown"]["text2"], justify = "left")
        
        # Error lost connection
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "contentBold", text = self._currentLanguage["errorLog"]["message"]["errorLostConnection"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["interact"]["errorLostConnection"]["text0"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["interact"]["errorLostConnection"]["text1"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["interact"]["errorLostConnection"]["text2"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["interact"]["errorLostConnection"]["text3"], justify = "left")

        