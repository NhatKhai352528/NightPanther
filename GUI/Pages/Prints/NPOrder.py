from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

def formatPrice(price: int):
    return "{:,.0f} VND".format(price, ",").replace(",", ".")

class NPOrder(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None, fileName: str = None, filePrice: int = None):

        self._currentLanguage = NPLanguage.getLanguage()
        
        super().__init__(master = master, commands = commands)
        
        # Passed variables handler
        self._fileName = fileName if fileName != None else ""
        self._filePrice = filePrice if filePrice != None else 0
        self._userCopies = 1
        self._userPrice = self._filePrice * self._userCopies
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = self._currentLanguage["order"]["data"]["title"], wrap = True)
        
        self._data.initText(mode = "heading", text = self._currentLanguage["order"]["data"]["text0"], wrap = False)
        self._fileNameIndex = self._data.initText(mode = "content", text = self._fileName, wrap = False)
        
        self._data.initText(mode = "heading", text = self._currentLanguage["order"]["data"]["text1"], wrap = False)
        self._filePriceIndex = self._data.initText(mode = "content", text = formatPrice(self._filePrice), wrap = False)
        
        self._data.initText(mode = "Heading", text = self._currentLanguage["order"]["data"]["text2"], wrap = False)
        self._userPriceIndex = self._data.initText(mode = "Content", text = formatPrice(self._userPrice), wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = self._currentLanguage["order"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = self._currentLanguage["order"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "content", text = "", justify = "left")
        self._interact.initText(mode = "heading", text = self._currentLanguage["order"]["interact"]["text0"], justify = "center")
        self._userCopiesIndex = self._interact.initSpinBox(default = self._userCopies, minimum = 1, maximum = 100, step = 1, wrap = False, actionCommand = None)
        self._userCopiesSpinBox = self._interact.npget(attribute = "spinBox", index = self._userCopiesIndex)
        self._userCopiesSpinBox.npset(attribute = "actionCommand", value = lambda event = None: self.npset(attribute = "userCopies", value = self._userCopiesSpinBox.npget(attribute = "value")))
    
    def npset(self, attribute: str, value: Any = None):
        if attribute == "fileName":
            self._fileName = value
            self._data.updateText(index = self._fileNameIndex, text = self._fileName)
        elif attribute == "filePrice":
            self._filePrice = value
            self._userPrice = self._filePrice * self._userCopies
            self._data.updateText(index = self._filePriceIndex, text = formatPrice(self._filePrice))
            self._data.updateText(index = self._userPriceIndex, text = formatPrice(self._userPrice))
        elif attribute == "userCopies":
            self._userCopies = value
            self._userPrice = self._filePrice * self._userCopies
            self._data.updateText(index = self._userPriceIndex, text = formatPrice(self._userPrice))
        elif attribute == "userPrice":
            self._userPrice = value
            self._data.updateText(index = self._userPriceIndex, text = formatPrice(self._userPrice))
    
    def npget(self, attribute: str):
        if attribute == "userCopies":
            return self._userCopies
        elif attribute == "userPrice":
            return self._userPrice