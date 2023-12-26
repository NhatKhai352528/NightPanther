from tkinter import Tk
from typing import Any
from ..NPPages import NPPages
from ...Customs.NPLanguage import NPLanguage
from ...Customs.NPTheme import NPTheme

class NPPrimary(NPPages):
    
    def __init__(self, master: Tk, commands: list[Any] = None):

        self._currentLanguage = NPLanguage.getLanguage()
        
        super().__init__(master = master, commands = commands)
        
        self._currentLanguageIndex = NPLanguage.getLanguageIndex()
        self._currentThemeIndex = NPTheme.getThemeIndex()
        
        languages = [["default", "default"]]
        themes = [["default", "default"]]
        languages[0][self._currentLanguageIndex] = "active"
        themes[0][self._currentThemeIndex] = "active"
        
        # Initialize items for data frame
        self._data.initText(mode = "title", text = self._currentLanguage["settingsInitial"]["data"]["title"], wrap = True)
        
        # Initialize items for control frame
        self._control.initButton(position = "left", command = self._commands[0], state = "normal", text = self._currentLanguage["settingsInitial"]["control"]["left"])
        self._control.initButton(position = "right", command = lambda event = None: self._saveSettings(), state = "normal", text = self._currentLanguage["settingsInitial"]["control"]["right"])
        
        # Initialize items for interact frame
        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = self._currentLanguage["settingsInitial"]["interact"]["text0"], justify = "center")
        self._languagesIndex = self._interact.initButtonArray(mode = "single", rows = 1, columns = 2, defaults = languages, texts = [["EN", "VN"]])
        self._languagesButtonArray = self._interact.npget(attribute = "buttonArray", index = self._languagesIndex)

        self._interact.initText(mode = "content", text = "", justify = "center")
        self._interact.initText(mode = "heading", text = self._currentLanguage["settingsInitial"]["interact"]["text1"], justify = "center")
        self._themesIndex = self._interact.initButtonArray(mode = "single", rows = 1, columns = 2, defaults = themes, texts = [[self._currentLanguage["settingsInitial"]["interact"]["light"], self._currentLanguage["settingsInitial"]["interact"]["dark"]]])
        self._themesButtonArray = self._interact.npget(attribute = "buttonArray", index = self._themesIndex)
    
    def _saveSettings(self):
        
        newLanguages = self._languagesButtonArray.npget(attribute = "active")
        newLanguageIndex = None
        
        for i in range(len(newLanguages[0])):
            if newLanguages[0][i] == True:
                newLanguageIndex = i
                break
        if newLanguageIndex != None:
            if newLanguageIndex != self._currentLanguageIndex:
                self._currentLanguageIndex = newLanguageIndex
                NPLanguage.setLanguage(languageCode = self._currentLanguageIndex)
        
        newThemes = self._themesButtonArray.npget(attribute = "active")
        newThemeIndex = None
        
        for i in range(len(newThemes[0])):
            if newThemes[0][i] == True:
                newThemeIndex = i
                break
        if newThemeIndex != None:
            if newThemeIndex != self._currentThemeIndex:
                self._currentThemeIndex = newThemeIndex
                NPTheme.setTheme(themeCode = self._currentThemeIndex)