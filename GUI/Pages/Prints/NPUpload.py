from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

currentLanguage = NPLanguage.getLanguage()

class NPUpload(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None, serverLink: str = None, serverKey: str = None, serverQRFile: str = None, fileName: str = None):
        
        super().__init__(master = master, commands = commands)
        
        # Passed variables handler
        self._serverLink = serverLink if serverLink != None else ""
        self._serverKey = serverKey if serverKey != None else ""
        self._serverQRFile = serverQRFile if serverQRFile != None else ""
        self._fileName = fileName if fileName != None else currentLanguage["upload"]["data"]["text4"]
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = currentLanguage["upload"]["data"]["title"], wrap = True)
        
        self._data.initText(mode = "heading", text = currentLanguage["upload"]["data"]["text0"], wrap = False)
        self._serverLinkIndex = self._data.initText(mode = "content", text = currentLanguage["upload"]["data"]["text1"] + self._serverLink, wrap = False)
        self._serverKeyIndex = self._data.initText(mode = "content", text = currentLanguage["upload"]["data"]["text2"] + self._serverKey, wrap = False)
        
        self._data.initText(mode = "Heading", text = currentLanguage["upload"]["data"]["text3"], wrap = False)
        self._fileNameIndex = self._data.initText(mode = "Content", text = self._fileName, wrap = True)
        
        # Initialize items for control frame
        # self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = currentLanguage["upload"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = currentLanguage["upload"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "heading", text = currentLanguage["upload"]["interact"]["text0"], justify = "center")
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._serverQRIndex = self._interact.initImage(imageFile = self._serverQRFile, imageWidth = 300, imageHeight = 300)
    
    def npset(self, attribute: str, value: Any = None):
        if attribute == "serverLink":
            self._serverLink = value
            self._data.updateText(index = self._serverLinkIndex, text = currentLanguage["upload"]["data"]["text1"] + self._serverLink)
        elif attribute == "serverKey":
            self._serverKey = value
            self._data.updateText(index = self._serverKeyIndex, text = currentLanguage["upload"]["data"]["text2"] + self._serverKey)
        elif attribute == "fileName":
            self._fileName = value
            self._data.updateText(index = self._fileNameIndex, text = self._fileName)
        elif attribute == "serverQRFile":
            self._serverQRFile = value
            self._interact.updateImage(index = self._serverQRIndex, imageFile = self._serverQRFile)