from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

currentLanguage = NPLanguage.getLanguage()

def formatPrice(price: int):
    return "{:,.0f} VND".format(price, ",").replace(",", ".")

class NPPayment(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None, fileName: str = None, userCopies: int = None, userPrice: int = None, userQRFile: str = None):
        
        super().__init__(master)
        
        # Passed commands handler
        self._commands = [Any, Any]
        try: 
            self._commands[0] = commands[0]
        except:
            self._commands[0] = None
        try: 
            self._commands[1] = commands[1]
        except:
            self._commands[1] = None
        
        # Passed variables handler
        self._fileName = fileName if fileName != None else ""
        self._userCopies = userCopies if userCopies != None else 0
        self._userPrice = userPrice if userPrice != None else 0
        self._userQRFile = userQRFile if userQRFile != None else ""
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = currentLanguage["payment"]["data"]["title"], wrap = True)
        
        self._data.initText(mode = "heading", text = currentLanguage["payment"]["data"]["text0"], wrap = False)
        self._fileNameIndex = self._data.initText(mode = "content", text = self._fileName, wrap = False)
        
        self._data.initText(mode = "heading", text = currentLanguage["payment"]["data"]["text1"], wrap = False)
        self._userCopiesIndex = self._data.initText(mode = "content", text = self._userCopies, wrap = False)
        
        self._data.initText(mode = "Heading", text = currentLanguage["payment"]["data"]["text2"], wrap = False)
        self._userPriceIndex = self._data.initText(mode = "Content", text = formatPrice(self._userPrice), wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = currentLanguage["payment"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = currentLanguage["payment"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "heading", text = currentLanguage["payment"]["interact"]["text0"], justify = "center")
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._userQRIndex = self._interact.initImage(imageFile = self._userQRFile, imageWidth = 300, imageHeight = 300)
    
    def npset(self, attribute: str, value: Any = None):
        if attribute == "fileName":
            self._fileName = value
            self._data.updateText(index = self._fileNameIndex, text = self._fileName)
        elif attribute == "userCopies":
            self._userCopies = value
            self._data.updateText(index = self._userCopiesIndex, text = self._userCopies)
        elif attribute == "userPrice":
            self._userPrice = value
            self._data.updateText(index = self._userPriceIndex, text = formatPrice(self._userPrice))
        elif attribute == "userQRFile":
            self._userQRFile = value
            self._interact.updateImage(index = self._userQRIndex, imageFile = self._userQRFile)