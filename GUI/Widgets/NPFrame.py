from tkinter import Frame, Tk
from typing import Any, Literal
from ..Customs.NPTheme import NPTheme

currentTheme = NPTheme.getTheme()

class NPFrame(Frame):
    
    def __init__(self, master: Frame | Tk, x: int, y: int, width: int, height: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str = currentTheme["background"]["default"]):
        
        # Location variables
        self._master = master
        self._x = int(x)
        self._y = int(y)
        self._width = int(width)
        self._height = int(height)
        
        self._anchor = anchor
        self._background = background
        super().__init__(master = self._master, background = self._background, borderwidth = 0, container = False, cursor = "arrow", highlightbackground = self._background, highlightcolor = self._background, highlightthickness = 0, relief = "flat", takefocus = False)
    
    def place(self):
        super().place(x = self._x, y = self._y, width = self._width, height = self._height, anchor = self._anchor)
    
    def destroy(self):
        super().destroy()
        self.__dict__.clear()
    
    def npset(self, attribute: str, value: Any):
        if attribute == "width":
            self._width = value