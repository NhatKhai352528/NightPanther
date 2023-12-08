from tkinter import Frame, Tk
from typing import Literal
from ..Customs.NPTheme import NPTheme

currentTheme = NPTheme.getTheme()

class NPFrame(Frame):
    
    def __init__(self, master: Frame | Tk, x: int, y: int, width: int, height: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str = currentTheme["background"]["default"]) -> None:
        
        # Location variables
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        
        self.anchor = anchor
        self.background = background
        super().__init__(master = master, background = self.background, borderwidth = 0, container = False, cursor = "arrow", highlightbackground = self.background, highlightcolor = self.background, highlightthickness = 0, relief = "flat", takefocus = False)
    
    def place(self):
        super().place(x = self.x, y = self.y, width = self.width, height = self.height, anchor = self.anchor)