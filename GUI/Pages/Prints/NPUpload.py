from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

currentLanguage = NPLanguage.getLanguage()

class NPUpload(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None, serverLink: str = None, serverKey: str = None, fileName: str = None):
        
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
        self._serverLink = serverLink
        self._serverKey = serverKey
        self._fileName = fileName
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = currentLanguage["upload"]["data"]["title"], wrap = True)
        self._data.initText(mode = "heading", text = currentLanguage["upload"]["data"]["text0"], wrap = False)
        self._serverLinkIndex = self._data.initText(mode = "content", text = currentLanguage["upload"]["data"]["text1"] + self._serverLink if self._serverLink != None else currentLanguage["upload"]["data"]["text1"], wrap = False)
        self._serverKeyIndex = self._data.initText(mode = "content", text = currentLanguage["upload"]["data"]["text2"] + self._serverKey if self._serverKey != None else currentLanguage["upload"]["data"]["text2"], wrap = False)
        self._data.initText(mode = "Heading", text = currentLanguage["upload"]["data"]["text3"], wrap = False)
        self._fileNameIndex = self._data.initText(mode = "Content", text = currentLanguage["upload"]["data"]["text4"] if self._fileName == None else self._fileName, wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = currentLanguage["upload"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = currentLanguage["upload"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "heading", text = currentLanguage["upload"]["interact"]["text0"], justify = "center")
        
    def update(self, serverLink: str = None, serverKey: str = None, fileName: str = None):
        
        if serverLink != None:
            self._serverLink = serverLink
            self._data.updateText(index = self._serverLinkIndex, text = currentLanguage["upload"]["data"]["text1"] + self._serverLink)
            
        if serverKey != None:
            self._serverKey = serverKey
            self._data.updateText(index = self._serverKeyIndex, text = currentLanguage["upload"]["data"]["text2"] + self._serverKey)
            
        if fileName != None:
            self._fileName = fileName
            self._data.updateText(index = self._fileNameIndex, text = self._fileName)