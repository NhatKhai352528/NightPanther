from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Constants.NPPaperPrice import PaperPrice
from ...Constants.NPInkPrice import InkPrice
from ...Constants.NPPaper import Paper
from ...Constants.NPSides import Sides
from .NPPrice import setInkPrice
from .NPPrice import setPaperPrice
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
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = self._currentLanguage["a4Price"]["interact"]["text0"], justify = "center")
        
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "content", text = self._currentLanguage["a4Price"]["interact"]["text1"], justify = "center")
        self._a4PaperPriceIndex = self._interact.initSpinBox(default = PaperPrice["a4"], minimum = 0, maximum = 5000, step = 100, wrap = True, actionCommand = None)
        self._a4PaperPriceSpinBox = self._interact.npget(attribute = "spinBox", index = self._a4PaperPriceIndex)
        if Paper["a4"]:
            self._a4PaperPriceSpinBox.npset(attribute = "actionCommand", value = lambda event = None: setPaperPrice("a4", self._a4PaperPriceSpinBox.npget(attribute = "value")))
        
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "content", text = self._currentLanguage["a4Price"]["interact"]["text2"], justify = "center")
        self._a4InkPriceIndex = self._interact.initSpinBox(default = InkPrice["a4"], minimum = 0, maximum = 5000, step = 100, wrap = True, actionCommand = None)
        self._a4InkPriceSpinBox = self._interact.npget(attribute = "spinBox", index = self._a4InkPriceIndex)
        if Paper["a4"]:
            self._a4InkPriceSpinBox.npset(attribute = "actionCommand", value = lambda event = None: setInkPrice("a4", self._a4InkPriceSpinBox.npget(attribute = "value")))
