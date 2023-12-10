from tkinter import Tk
from typing import Literal
from .NPFrames import NPFrames
from ..Constants.NPScreen import Status
from ..Customs.NPTheme import NPTheme
from ..Widgets.NPImageLabel import NPImageLabel
from ..Widgets.NPTextLabel import NPTextLabel

currentTheme = NPTheme.getTheme()

class NPStatus(NPFrames):
    
    def __init__(self, master: Tk):
        
        super().__init__(master = master, x = Status["x"], y = Status["y"], width = Status["width"], height = Status["height"], distance = Status["distance"], anchor = "nw", background = currentTheme["background"]["status"])
        
        self._currentLeft = self._distance
        self._currentRight = self._width - self._distance
        
        
    def initImage(self, anchor: Literal["w", "e"], imageFile: str):
        
        # Get current index
        currentIndex = len(self._items)
        
        # Only small squared icons allowed
        imageHeight = self._height - 2 * self._distance
        imageWidth = imageHeight
        
        self._items.append(NPImageLabel(master = self._frame, x = self._currentLeft if anchor == "w" else self._currentRight, y = 0.5 * self._height, anchor = anchor, background = self.npget("background"), imageFile = imageFile, imageWidth = imageWidth, imageHeight = imageHeight))
        
        # This frame does not allow items to exceed its boundaries or override others
        if anchor == "w":
            if self._currentLeft + self._items[currentIndex].npget("width") + self._distance > self._currentRight:
                self._items[currentIndex].destroy()
                return None
            else:
                self._items[currentIndex].place()
                self._currentLeft = self._currentLeft + self._items[currentIndex].npget("width") + self._distance
                return currentIndex
        elif anchor == "e":
            if self._currentRight - self._items[currentIndex].npget("height") - self._distance < self._currentLeft:
                self._items[currentIndex].destroy()
                return None
            else:
                self._items[currentIndex].place()
                self._currentRight = self._currentRight - self._items[currentIndex].npget("height") - self._distance
                return currentIndex
    
    def updateImage(self, index: int, imageFile: str):
        
        if index >= len(self._items):
            return
        if not isinstance(self._items[index], NPImageLabel):
            return
        self._items[index].npset(attribute = "imageFile", value = imageFile)
    
    def initText(self, width: int, anchor: Literal["w", "e"], text: str):
        
        # Get current index
        currentIndex = len(self._items)
        
        # Get current font and foreground
        currentFont = currentTheme["font"]["strong"]
        currentForeground = currentTheme["foreground"]["inverse"]
        
        # Define a new text label, place it onto the frame, and update position for the next item
        self._items.append(NPTextLabel(master = self._frame, x = self._currentLeft if anchor == "w" else self._currentRight, y = 0.5 * self._height, width = width, anchor = anchor, background = self.npget("background"), font = currentFont, foreground = currentForeground, justify = "left" if anchor == "w" else "right", text = text, textAnchor = anchor, underline = -1, wraplength = 0))
        
        # This frame does not allow items to exceed its boundaries or override others
        if anchor == "w":
            if self._currentLeft + self._items[currentIndex].npget("width") + self._distance > self._currentRight:
                self._items[currentIndex].destroy()
                return None
            else:
                self._items[currentIndex].place()
                self._currentLeft = self._currentLeft + self._items[currentIndex].npget("width") + self._distance
                return currentIndex
        elif anchor == "e":
            if self._currentRight - self._items[currentIndex].npget("height") - self._distance < self._currentLeft:
                self._items[currentIndex].destroy()
                return None
            else:
                self._items[currentIndex].place()
                self._currentRight = self._currentRight - self._items[currentIndex].npget("height") - self._distance
    
    def updateText(self, index: int, text: str):
        
        if index >= len(self._items):
            return
        if not isinstance(self._items[index], NPTextLabel):
            return
        self._items[index].npset(attribute = "text", value = text)
