from tkinter import Frame, Message
from tkinter.font import Font
from typing import Any, Literal
from ..Customs.NPTheme import NPTheme

defaultTheme = NPTheme.getTheme()

class NPMessage(Message):
    
    def __init__(self, master: Frame, x: int, y: int, width: int, height: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str = defaultTheme["background"]["default"], font: Font = defaultTheme["font"]["default"], foreground: str = defaultTheme["foreground"]["default"], text: str = "Test"):
        
        # Location variables
        self._master = master
        self._x = int(x)
        self._y = int(y)
        self._width = int(width)
        self._height = int(height)
        
        self._anchor = anchor
        self._background = background
        
        self._font = font
        self._foreground = foreground
        self._text = text
    
        super().__init__(master = self._master, anchor = "center", aspect = int(self._width / self._height * 100), background = self._background, borderwidth = 0, cursor = "arrow", font = self._font, foreground = self._foreground, highlightbackground = self._background, highlightcolor = self._background, highlightthickness = 0, justify = "center", relief = "flat", takefocus = False, text = self._text, textvariable = None)
    
    def place(self):
        super().place(x = self._x, y = self._y, width = self._width, height = self._height, anchor = self._anchor)
    
    def destroy(self):
        super().destroy()
        self.__dict__.clear()
    
    def npset(self, attribute: str, value: Any = None):
        if attribute == "text":
            self._text = value
            super().configure(text = self._text)
    
    def npget(self, attribute: str):
        if attribute == "width":
            return self._width
        if attribute == "height":
            return self._height