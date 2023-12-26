from tkinter import Frame, Label
from tkinter.font import Font
from typing import Any, Literal
from ..Customs.NPTheme import NPTheme

defaultTheme = NPTheme.getTheme()

class NPTextLabel(Label):
    
    def __init__(self, master: Frame, x: int, y: int, width: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str = defaultTheme["background"]["default"], font: Font = defaultTheme["font"]["default"], foreground: str = defaultTheme["foreground"]["default"], justify: Literal["left", "center", "right"] = "left", text: str = None, textAnchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"] = "nw", underline: int = -1, wraplength: int = 0):
        
        # Location variables
        self._master = master
        self._x = int(x)
        self._y = int(y)
        self._width = int(width)
        
        self._anchor = anchor
        self._background = background
        
        # Text variables
        self._font = font
        self._foreground = foreground
        self._justify = justify
        self._text = text
        self._textAnchor = textAnchor
        self._underline = underline
        self._wraplength = wraplength
        
        if self._wraplength == 0:
            self._rewrite()
        
        super().__init__(master = self._master, activebackground = self._background, activeforeground = self._foreground, anchor = self._textAnchor, background = self._background, bitmap = None, borderwidth = 0, compound = "center", cursor = "arrow", disabledforeground = self._foreground, font = self._font, foreground = self._foreground, highlightbackground = self._background, highlightcolor = self._background, highlightthickness = 0, image = None, justify = self._justify, relief = "flat", state = "normal", takefocus = False, text = self._text, textvariable = None, underline = self._underline, wraplength = self._wraplength)

    def _rewrite(self):
        textWidth = self._font.measure(self._text)
        if textWidth > self._width:
            while textWidth > self._width - self._font.measure("..."):
                self._text = self._text[:-1]
                textWidth = self._font.measure(self._text)
            self._text = self._text + "..."
    
    def place(self):
        super().place(x = self._x, y = self._y, width = self._width, anchor = self._anchor)
    
    def destroy(self):
        super().destroy()
        self.__dict__.clear()
    
    def npset(self, attribute: str, value: Any = None):
        if attribute == "text":
            self._text = value
            if self._wraplength == 0:
                self._rewrite()
            super().configure(text = self._text)
    
    def npget(self, attribute: str):
        if attribute == "width":
            return self._width
        if attribute == "height":
            return super().winfo_reqheight()