from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

class NPTutorial2(NPPages):
    
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
        
        # Error file
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "contentBold", text = self._currentLanguage["errorLog"]["message"]["errorPrintFile"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["interact"]["errorPrintFile"]["text0"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["interact"]["errorPrintFile"]["text1"], justify = "left")

        # Error wrong transfer amount
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "contentBold", text = self._currentLanguage["errorLog"]["message"]["errorTransferAmount"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["interact"]["errorTransferAmount"]["text0"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["interact"]["errorTransferAmount"]["text1"], justify = "left")

        # Error Payment checking system
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "contentBold", text = self._currentLanguage["errorLog"]["message"]["errorPaymentCheck"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["interact"]["errorPaymentCheck"]["text0"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["adminInstruction"]["interact"]["errorPaymentCheck"]["text1"], justify = "left")