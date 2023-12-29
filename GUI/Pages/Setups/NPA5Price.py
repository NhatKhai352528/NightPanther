from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Constants.NPPaperPrice import PaperPrice
from ...Constants.NPInkPrice import InkPrice
from ...Constants.NPPaper import Paper
from ...Constants.NPSides import Sides
from .NPPrice import setPaperPrice
from .NPPrice import setInkPrice
from ...Customs.NPLanguage import NPLanguage

class NPA5Price(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None):

        self._currentLanguage = NPLanguage.getLanguage()
        
        super().__init__(master = master, commands = commands)
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = self._currentLanguage["a5Price"]["data"]["title"], wrap = True)
        self._data.initText(mode = "Content", text = self._currentLanguage["a5Price"]["data"]["text0"], wrap = True)
        self._data.initText(mode = "content", text= self._currentLanguage["a5Price"]["data"]["text1"], wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = self._currentLanguage["a5Price"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = self._currentLanguage["a5Price"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = self._currentLanguage["a5Price"]["interact"]["text0"], justify = "center")
        
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "content", text = self._currentLanguage["a5Price"]["interact"]["text1"], justify = "center")
        self._a5PaperPriceIndex = self._interact.initSpinBox(default = PaperPrice["a5"], minimum = 0, maximum = 5000, step = 100, wrap = True, actionCommand = None)
        self._a5PaperPriceSpinBox = self._interact.npget(attribute = "spinBox", index = self._a5PaperPriceIndex)
        if Paper["a5"] and Sides["1s"]:
            self._a5PaperPriceSpinBox.npset(attribute = "actionCommand", value = lambda event = None: setPaperPrice("a5", self._a5PaperPriceSpinBox.npget(attribute = "value")))
        
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "content", text = self._currentLanguage["a5Price"]["interact"]["text2"], justify = "center")
        self._a5InkPriceIndex = self._interact.initSpinBox(default = InkPrice["a5"], minimum = 0, maximum = 5000, step = 100, wrap = True, actionCommand = None)
        self._a5InkPriceSpinBox = self._interact.npget(attribute = "spinBox", index = self._a5InkPriceIndex)
        if Paper["a5"] and Sides["2s"]:
            self._a5InkPriceSpinBox.npset(attribute = "actionCommand", value = lambda event = None: setInkPrice("a5", self._a5InkPriceSpinBox.npget(attribute = "value")))
