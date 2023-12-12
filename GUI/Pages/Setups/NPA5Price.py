from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Constants.NPPrice import Price
from ...Customs.NPLanguage import NPLanguage

currentLanguage = NPLanguage.getLanguage()

class NPA5Price(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None):
        
        super().__init__(master = master, commands = commands)
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = currentLanguage["a5Price"]["data"]["title"], wrap = True)
        self._data.initText(mode = "Content", text = currentLanguage["a5Price"]["data"]["text0"], wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = currentLanguage["a5Price"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = currentLanguage["a5Price"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = currentLanguage["a5Price"]["interact"]["text0"], justify = "center")
        
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._a51sPriceIndex = self._interact.initSpinBox(default = Price["a5"]["1s"], minimum = 0, maximum = 5000, step = 100, wrap = True, actionCommand = None)
        self._a51sPriceSpinBox = self._interact.npget(attribute = "spinBox", index = self._a51sPriceIndex)
        
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._a52sPriceIndex = self._interact.initSpinBox(default = Price["a5"]["2s"], minimum = 0, maximum = 5000, step = 100, wrap = True, actionCommand = None)
        self._a52sPriceSpinBox = self._interact.npget(attribute = "spinBox", index = self._a52sPriceIndex)
