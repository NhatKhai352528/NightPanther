from tkinter import Frame
from typing import Any, Literal
from ..NPFrames import NPFrames
from ...Constants.NPWorkspace import Menu
from ...Customs.NPTheme import NPTheme
from ...Widgets.NPImageButton import NPImageButton

currentTheme = NPTheme.getTheme()

class NPMenu(NPFrames):
    
    def __init__(self, master: Frame):
        
        super().__init__(master = master, x = Menu["x"], y = Menu["y"], width = Menu["width"], height = Menu["height"], distance = Menu["distance"], anchor = "nw", background = currentTheme["background"]["menu"])
        
        # In order to get a good visual, the self._widthSize must be approximate to the self._heightSize
        self._widthSize = int((self._width - 5 * self._distance) / 4)
        self._heightSize = int(self._height - 2 * self._distance)
        
        # There are at most 4 buttons in this frame
        self._currentItems = [None, None, None, None]
    
    def initButton(self, index: Literal[0, 1, 2, 3], command: Any, imageFile: str, state: Literal["normal", "disabled"]):
        
        # Get current index and return if the button at the same position exists
        currentIndex = len(self._items)
        if self._currentItems[index] != None:
            return
        
        # Define a new button and place it onto the frame
        self._items.append(NPImageButton(master = self._frame, mode = "action", x = index * self._widthSize + (index + 1) * self._distance, y = self._distance, width = self._widthSize, height = self._heightSize, anchor = "nw", command = command, imageFile = imageFile, repeat = False, state = state))
        self._items[currentIndex].place()
        
        return currentIndex