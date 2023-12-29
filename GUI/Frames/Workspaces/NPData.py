from tkinter import Tk
from typing import Literal
from ..NPFrames import NPFrames
from ...Constants.NPWorkspace import Data
from ...Customs.NPTheme import NPTheme
from ...Widgets.NPTextLabel import NPTextLabel

class NPData(NPFrames):
    
    def __init__(self, master: Tk):

        self._currentTheme = NPTheme.getTheme()
        
        super().__init__(master = master, x = Data["x"], y = Data["y"], width = Data["width"], height = Data["height"], distance = Data["distance"], anchor = "nw", background = self._currentTheme["background"]["data"])
        
        self._currentY = self._distance
    
    def initText(self, mode: Literal["title", "Heading", "heading", "Content", "content"], text: str, wrap: bool):
        
        # This frame allows the last item to exceed its boundaries
        if self._currentY >= self._height:
            return None
        
        # Get current index, font anf foreground
        currentIndex = len(self._items)
        if mode == "title":
            currentFont = self._currentTheme["font"]["title"]
            currentForeground = self._currentTheme["foreground"]["highlight"]
        elif mode == "Heading":
            currentFont = self._currentTheme["font"]["strong"]
            currentForeground = self._currentTheme["foreground"]["highlight"]
        elif mode == "heading":
            currentFont = self._currentTheme["font"]["strong"]
            currentForeground = self._currentTheme["foreground"]["default"]
        elif mode == "Content":
            currentFont = self._currentTheme["font"]["normal"]
            currentForeground = self._currentTheme["foreground"]["highlight"]
        elif mode == "content":
            currentFont = self._currentTheme["font"]["normal"]
            currentForeground = self._currentTheme["foreground"]["default"]
        else:
            currentFont = self._currentTheme["font"]["default"]
            currentForeground = self._currentTheme["foreground"]["default"]
        
        # Define a new text label, place it onto the frame, and update position for the next item
        self._items.append(NPTextLabel(master = self._frame, x = self._distance, y = self._currentY, width = self._width - 2 * self._distance, anchor = "nw", background = self._currentTheme["background"]["default"], font = currentFont, foreground = currentForeground, justify = "left", text = text, textAnchor = "nw", underline = -1, wraplength = 0 if wrap == False else self._width - 2 * self._distance))
        self._items[currentIndex].place()
        self._currentY = self._currentY + self._items[currentIndex].npget(attribute = "height")
        
        return currentIndex
    
    def updateText(self, index: int, text: str):
        if index >= len(self._items):
            return
        if not isinstance(self._items[index], NPTextLabel):
            return
        self._items[index].npset(attribute = "text", value = text)