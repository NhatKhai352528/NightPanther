from tkinter import Frame
from typing import Literal
from ..NPFrames import NPFrames
from ...Constants.NPWorkspace import Data
from ...Customs.NPTheme import NPTheme
from ...Widgets.NPTextLabel import NPTextLabel

currentTheme = NPTheme.getTheme()

class NPData(NPFrames):
    
    def __init__(self, master: Frame):
        
        super().__init__(master = master, x = Data["x"], y = Data["y"], width = Data["width"], height = Data["height"], distance = Data["distance"], anchor = "nw", background = currentTheme["background"]["data"])
        
        self._currentY = self._distance
    
    def initText(self, mode: Literal["title", "Heading", "heading", "Content", "content"], text: str, wrap: bool):
        
        # This frame allows the last item to exceed its boundaries
        if self._currentY >= self._height:
            return None
        
        # Get current index, font anf foreground
        currentIndex = len(self._items)
        if mode == "title":
            currentFont = currentTheme["font"]["title"]
            currentForeground = currentTheme["foreground"]["highlight"]
        elif mode == "Heading":
            currentFont = currentTheme["font"]["strong"]
            currentForeground = currentTheme["foreground"]["highlight"]
        elif mode == "heading":
            currentFont = currentTheme["font"]["strong"]
            currentForeground = currentTheme["foreground"]["default"]
        elif mode == "Content":
            currentFont = currentTheme["font"]["normal"]
            currentForeground = currentTheme["foreground"]["highlight"]
        elif mode == "content":
            currentFont = currentTheme["font"]["normal"]
            currentForeground = currentTheme["foreground"]["default"]
        
        # Define a new text label, place it onto the frame, and update position for the next item
        self._items.append(NPTextLabel(master = self._frame, x = self._distance, y = self._currentY, width = self._width - 2 * self._distance, anchor = "nw", background = currentTheme["background"]["default"], font = currentFont, foreground = currentForeground, justify = "left", text = text, textAnchor = "nw", underline = -1, wraplength = 0 if wrap == False else self._width - 2 * self._distance))
        self._items[currentIndex].place()
        self._currentY = self._currentY + self._items[currentIndex].npget("height")
        
        return currentIndex
    
    def updateText(self, index: int, text: str):
        if index >= len(self._items):
            return
        if not isinstance(self._items[index], NPTextLabel):
            return
        self._items[index].npset(attribute = "text", value = text)