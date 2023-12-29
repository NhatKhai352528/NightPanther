from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Constants.NPPrice import Price
from ...Constants.NPPaper import Paper
from ...Constants.NPSides import Sides
from .NPPrice import setPrice
from ...Customs.NPLanguage import NPLanguage

class NPA4Price(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None):

        self._currentLanguage = NPLanguage.getLanguage()
        
        super().__init__(master = master, commands = commands)
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = self._currentLanguage["a4Price"]["data"]["title"], wrap = True)
        self._data.initText(mode = "Content", text = self._currentLanguage["a4Price"]["data"]["text0"], wrap = True)
        self._data.initText(mode = "content", text= self._currentLanguage["a4Price"]["data"]["text1"], wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = self._currentLanguage["a4Price"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = self._currentLanguage["a4Price"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = self._currentLanguage["a4Price"]["interact"]["text0"], justify = "center")
        
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "content", text = self._currentLanguage["a4Price"]["interact"]["text1"], justify = "center")
        self._a41sPriceIndex = self._interact.initSpinBox(default = Price["a4"]["1s"], minimum = 0, maximum = 5000, step = 100, wrap = True, actionCommand = None)
        self._a41sPriceSpinBox = self._interact.npget(attribute = "spinBox", index = self._a41sPriceIndex)
        if Paper["a4"] and Sides["1s"]:
            self._a41sPriceSpinBox.npset(attribute = "actionCommand", value = lambda event = None: setPrice("a4", "1s", self._a41sPriceSpinBox.npget(attribute = "value")))
        
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "content", text = self._currentLanguage["a4Price"]["interact"]["text2"], justify = "center")
        self._a42sPriceIndex = self._interact.initSpinBox(default = Price["a4"]["2s"], minimum = 0, maximum = 5000, step = 100, wrap = True, actionCommand = None)
        self._a42sPriceSpinBox = self._interact.npget(attribute = "spinBox", index = self._a42sPriceIndex)
        if Paper["a4"] and Sides["2s"]:
            self._a42sPriceSpinBox.npset(attribute = "actionCommand", value = lambda event = None: setPrice("a4", "2s", self._a42sPriceSpinBox.npget(attribute = "value")))
