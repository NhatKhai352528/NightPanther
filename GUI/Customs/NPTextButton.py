from tkinter import Button, Frame
from tkinter.font import Font
from typing import Any, Literal
from Customs.NPTheme import NPTheme

currentTheme = NPTheme.getTheme()

class NPTextButton(Button):
    
    def __init__(self, master: Frame, mode: Literal["input", "action"], x: int, y: int, width: int, height: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], command: Any = None, font: Font = currentTheme["font"]["normal"], repeat: bool = False, state: Literal["normal", "disabled"] = "normal", text: str = None) -> None:
        
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.anchor = anchor
        
        self.mode = mode
        currentTheme = NPTheme.getTheme()
        
        self.foreground = currentTheme["foreground"]["inverse"]
        
        if self.mode == "input":
            self.background = currentTheme["inputButton"]["default"]
            self.activebackground = currentTheme["inputButton"]["active"]
            self.disabledbackground = currentTheme["inputButton"]["disabled"]
        elif self.mode == "action":
            self.background = currentTheme["actionButton"]["default"]
            self.activebackground = currentTheme["actionButton"]["active"]
            self.disabledbackground = currentTheme["actionButton"]["disabled"]
        
        super().__init__(master, activebackground = self.activebackground, activeforeground = self.foreground, anchor = "center", background = self.background if state == "normal" else self.disabledbackground, bitmap = None, borderwidth = 0, command = command, compound = "center", cursor = "arrow", default = "normal", disabledforeground = self.foreground, font = font, foreground = self.foreground, highlightbackground = self.background, highlightcolor = self.background, highlightthickness = 0, image = None, justify = "center", overrelief = "flat", relief = "flat", repeatdelay = 1000, repeatinterval = 0 if repeat == False else 100, state = state, takefocus = False, text = text, textvariable = None, underline = -1, wraplength = 0)
    
    def place(self):
        super().place(x = self.x, y = self.y, width = self.width, height = self.height, anchor = self.anchor)