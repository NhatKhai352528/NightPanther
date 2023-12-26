from tkinter import Tk
from typing import Any, Literal
from ..NPFrames import NPFrames
from ...Constants.NPWorkspace import Control
from ...Customs.NPTheme import NPTheme
from ...Widgets.NPTextButton import NPTextButton

currentTheme = NPTheme.getTheme()

class NPControl(NPFrames):
    
    def __init__(self, master: Tk):
        
        super().__init__(master = master, x = Control["x"], y = Control["y"], width = Control["width"], height = Control["height"], distance = Control["distance"], anchor = "nw", background = currentTheme["background"]["control"])
        
        self._widthSize = int((self._width - 3 * self._distance) / 2)
        self._heightSize = int(self._height - 2 * self._distance)
        
        # There are at most 2 buttons in this frame
        self._currentItems = [None, None]
    
    def initButton(self, position: Literal["left", "right"], command: Any, state: Literal["normal", "disabled"], text: str):
        
        # Get current index and delete the button at the same position if it exists
        currentIndex = len(self._items)
        if position == "left":
            if self._currentItems[0] != None:
                self._items[self._currentItems[0]].destroy()
            self._currentItems[0] = currentIndex
        elif position == "right":
            if self._currentItems[1] != None:
                self._items[self._currentItems[1]].destroy()
            self._currentItems[1] = currentIndex
        
        # Define a new button and place it onto the frame
        self._items.append(NPTextButton(master = self._frame, mode = "action", x = self._distance if position == "left" else self._width - self._distance, y = self._distance, width = self._widthSize, height = self._heightSize, anchor = "nw" if position == "left" else "ne", command = command, font = currentTheme["font"]["strong"], repeat = False, state = state, text = text))
        self._items[currentIndex].place()
        
        return currentIndex