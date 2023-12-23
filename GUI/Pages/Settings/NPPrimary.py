from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage
from ...Customs.NPTheme import NPTheme

currentLanguage = NPLanguage.getLanguage()
currentTheme = NPTheme.getTheme()

class NPPrimary(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any] = None):
        
        super().__init__(master = master, commands = commands)
        
        self._availableLanguages = NPLanguage.getLanguages()
        self._availableThemes = NPTheme.getThemes()
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = currentLanguage["settingsInitial"]["data"]["title"], wrap = True)
        self._data.initText(mode = "Content", text = currentLanguage["settingsInitial"]["data"]["text0"], wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = currentLanguage["settingsInitial"]["control"]["left"])
        self._control.initButton(position = "right", command = lambda event = None: self._master.destroy(), state = "normal", text = currentLanguage["settingsInitial"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = currentLanguage["settingsInitial"]["interact"]["text0"], justify = "center")
        self._interact.initButtonArray(mode = "single", rows = 1, columns = 2, defaults = None, texts = [["VN", "EN"]])
        
        # self._interact.initText(mode = "content", text = "", justify = "center")
        # self._interact.initText(mode = "heading", text = currentLanguage["settingsInitial"]["interact"]["text0"], justify = "center")
        # self._interact.initButtonArray(mode = "single", rows = 1, columns = 2, defaults = None, texts = [["Hah", "Huh"]])