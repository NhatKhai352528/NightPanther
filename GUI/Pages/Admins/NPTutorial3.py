from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

class NPTutorial3(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None):

        self._currentLanguage = NPLanguage.getLanguage()
        
        super().__init__(master = master, commands = commands)
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = self._currentLanguage["adminInstruction"]["data"]["title"], wrap = True)
        self._data.initText(mode = "Content", text = self._currentLanguage["adminInstruction"]["data"]["subtitle"], wrap = True)
        self._data.initText(mode = "content", text = self._currentLanguage["adminInstruction"]["data"]["text1"], wrap = True)
        self._data.initText(mode = "content", text = self._currentLanguage["adminInstruction"]["data"]["text2"], wrap = True)

        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = self._currentLanguage["adminInstruction"]["control"]["back"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = self._currentLanguage["adminInstruction"]["control"]["start"])
        
        # Initialize items for interact frame
        # Error file
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = self._currentLanguage["errorLog"]["message"]["errorPaperStuck"], justify = "left")
        self._interact.initText(mode = "small", text = self._currentLanguage["adminInstruction"]["interact"]["errorPaperStuck"]["text0"], justify = "left")
        self._interact.initText(mode = "small", text = self._currentLanguage["adminInstruction"]["interact"]["errorPaperStuck"]["text1"], justify = "left")

        # Error wrong transfer amount
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = self._currentLanguage["errorLog"]["message"]["errorOutOfPaper"], justify = "left")
        self._interact.initText(mode = "small", text = self._currentLanguage["adminInstruction"]["interact"]["errorOutOfPaper"]["text0"], justify = "left")
        self._interact.initText(mode = "small", text = self._currentLanguage["adminInstruction"]["interact"]["errorOutOfPaper"]["text1"], justify = "left")