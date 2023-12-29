from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Constants.NPSides import Sides
from ...Customs.NPLanguage import NPLanguage

class NPSides(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None):

        self._currentLanguage = NPLanguage.getLanguage()
        
        super().__init__(master = master, commands = commands)
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = self._currentLanguage["sides"]["data"]["title"], wrap = True)
        self._data.initText(mode = "Content", text = self._currentLanguage["sides"]["data"]["text0"], wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = self._currentLanguage["sides"]["control"]["left"])
        self._control.initButton(position = "right", command = lambda event = None: self._saveAvailableSides(), state = "normal", text = self._currentLanguage["sides"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = self._currentLanguage["sides"]["interact"]["text0"], justify = "center")
        self._interact.initText(mode = "content", text = self._currentLanguage["paper"]["interact"]["text1"], justify = "center")
        
        availableSides = [["active" if value else "default" for value in Sides.values()]]
        
        self._interact.initText(mode = "footnote", text = "", justify = "center")
        self._availableSidesIndex = self._interact.initButtonArray(mode = "multiple", rows = 1, columns = 2, defaults = availableSides, texts = [["1", "2"]])
        self._availableSidesButtonArray = self._interact.npget(attribute = "buttonArray", index = self._availableSidesIndex)
    
    def _saveAvailableSides(self):
        currentActive = self._availableSidesButtonArray.npget(attribute = "active")
        for (side, active) in zip(Sides.keys(), currentActive[0]):
            Sides[side] = active
        self._currentActive = currentActive
        with open("GUI/Constants/NPSides.py", "w") as file:
            file.write("Sides = " + repr(Sides))
