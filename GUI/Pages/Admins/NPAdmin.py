from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage

class NPAdmin(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any, Any] = None, switchCommands: list[Any] = None):

        self._currentLanguage = NPLanguage.getLanguage()
        
        super().__init__(master = master, commands = commands)

        # Passed switchCommands handler
        self._switchCommands = [Any, Any, Any, Any]
        for i in range(4):
            try:
                self._switchCommands[i] = switchCommands[i]
            except:
                self._switchCommands[i] = None
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = self._currentLanguage["helpInitial"]["data"]["title"], wrap = True)
        self._data.initText(mode = "content", text = self._currentLanguage["helpInitial"]["data"]["text1"], wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = self._currentLanguage["helpInitial"]["control"]["left"])
        self._control.initButton(position = "right", command = self._commands[1], state = "normal", text = self._currentLanguage["helpInitial"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = self._currentLanguage["helpInitial"]["interact"]["text0"], justify = "center")
        
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._firstSwitchIndex = self._interact.initButton(command = self._switchCommands[0], text = self._currentLanguage["helpInitial"]["interact"]["text1"])
        
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._secondSwitchIndex = self._interact.initButton(command = self._switchCommands[1], text = self._currentLanguage["helpInitial"]["interact"]["text2"])
        
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._thirdSwitchIndex = self._interact.initButton(command = self._switchCommands[2], text = self._currentLanguage["helpInitial"]["interact"]["text3"])
        
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._fourthSwitchIndex = self._interact.initButton(command = self._switchCommands[3], text = self._currentLanguage["helpInitial"]["interact"]["text4"])