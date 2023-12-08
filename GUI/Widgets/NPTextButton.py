from tkinter import Button, Frame
from tkinter.font import Font
from typing import Any, Literal
from ..Customs.NPTheme import NPTheme

currentTheme = NPTheme.getTheme()

currentTheme = NPTheme.getTheme()
        
class NPTextButton(Button):
    
    def __init__(self, master: Frame, mode: Literal["input", "action", "select"], x: int, y: int, width: int, height: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], command: Any = None, font: Font = currentTheme["font"]["default"], repeat: bool = False, state: Literal["normal", "disabled"] = "normal", text: str = None) -> None:
        
        # Mode variables
        self.mode = mode
        
        # Location variables
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.anchor = anchor
        
        # Theme variables
        self.foreground = currentTheme["foreground"]["inverse"]
        self.background = currentTheme["button"][self.mode]["default"]
        self.activebackground = currentTheme["button"][self.mode]["active"]
        self.disabledbackground = currentTheme["button"][self.mode]["disabled"]
        
        super().__init__(master = master, activebackground = self.activebackground, activeforeground = self.foreground, anchor = "center", background = self.background if state == "normal" else self.disabledbackground, bitmap = None, borderwidth = 0, command = command, compound = "center", cursor = "arrow", default = "normal", disabledforeground = self.foreground, font = font, foreground = self.foreground, highlightbackground = self.background, highlightcolor = self.background, highlightthickness = 0, image = None, justify = "center", overrelief = "flat", relief = "flat", repeatdelay = 1000, repeatinterval = 0 if repeat == False else 10, state = state, takefocus = False, text = text, textvariable = None, underline = -1, wraplength = 0)
        
    def place(self):
        super().place(x = self.x, y = self.y, width = self.width, height = self.height, anchor = self.anchor)
        
    def setText(self, text: str = None):
        if text != None:
            super().configure(text = text)