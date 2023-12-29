from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

class NPPay(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None):

        self._currentLanguage = NPLanguage.getLanguage()
        
        super().__init__(master = master, commands = commands)
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = self._currentLanguage["helpPay"]["data"]["title"], wrap = True)
        self._data.initText(mode = "content", text = self._currentLanguage["helpPay"]["data"]["text0"], wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = self._currentLanguage["helpPay"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = self._currentLanguage["helpPay"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "contentBold", text = self._currentLanguage["helpPay"]["interact"]["text0"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["helpPay"]["interact"]["text1"], justify = "left")
        
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "contentBold", text = self._currentLanguage["helpPay"]["interact"]["text2"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["helpPay"]["interact"]["text3"], justify = "left")

        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "contentBold", text = self._currentLanguage["helpPay"]["interact"]["text4"], justify = "left")
        self._interact.initText(mode = "smallThin", text = self._currentLanguage["helpPay"]["interact"]["text5"], justify = "left")
