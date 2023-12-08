from tkinter import Frame, Label
from tkinter.font import Font
from typing import Literal
from Customs.NPTheme import NPTheme

currentTheme = NPTheme.getTheme()

class NPTextLabel(Label):
    
    def __init__(self, master: Frame, x: int, y: int, width: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str = currentTheme["background"]["default"], font: Font = currentTheme["font"]["default"], foreground: str = currentTheme["foreground"]["default"], justify: Literal["left", "center", "right"] = "left", text: str = None, textAnchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"] = "nw", underline: int = -1, wraplength: int = 0) -> None:
        
        # Location variables
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.anchor = anchor
        
        super().__init__(master = master, activebackground = background, activeforeground = foreground, anchor = textAnchor, background = background, bitmap = None, borderwidth = 0, compound = "center", cursor = "arrow", disabledforeground = foreground, font = font, foreground = foreground, highlightbackground = background, highlightcolor = background, highlightthickness = 0, image = None, justify = justify, relief = "flat", state = "normal", takefocus = False, text = text, textvariable = None, underline = underline, wraplength = wraplength)
    
    def place(self):
        super().place(x = self.x, y = self.y, width = self.width, anchor = self.anchor)
        
    def setText(self, text: str = None):
        if text != None:
            super().configure(text = text)
    
    def getHeight(self):
        return self.winfo_reqheight()