from tkinter import Button, Frame
from typing import Any, Literal
from Customs.NPTheme import NPTheme
from Widgets.NPImage import NPImage

currentTheme = NPTheme.getTheme()

class NPImageButton(Button):
    
    def __init__(self, master: Frame, mode: Literal["input", "action", "select"], x: int, y: int, width: int, height: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], command: Any = None, imageFile: str = None, repeat: bool = False, state: Literal["normal", "disabled"] = "normal") -> None:
        
        # Mode variables
        self.mode = mode
        
        # Location variables
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.anchor = anchor
        
        # Image variables
        self.imageFile = imageFile
        self.image = NPImage(file = self.imageFile, width = 0.8 * self.width, height = 0.8 * self.height)
        
        # Theme variables
        self.background = currentTheme["button"][self.mode]["default"]
        self.activebackground = currentTheme["button"][self.mode]["active"]
        self.disabledbackground = currentTheme["button"][self.mode]["disabled"]
        
        super().__init__(master, activebackground = self.activebackground, activeforeground = None, anchor = "center", background = self.background if state == "normal" else self.disabledbackground, bitmap = None, borderwidth = 0, command = command, compound = "center", cursor = "arrow", default = "normal", disabledforeground = None, font = None, foreground = None, highlightbackground = self.background, highlightcolor = self.background, highlightthickness = 0, image = self.image.image, justify = "center", overrelief = "flat", relief = "flat", repeatdelay = 1000, repeatinterval = 0 if repeat == False else 10, state = state, takefocus = False, text = None, textvariable = None, underline = -1, wraplength = 0)
    
    def place(self):
        super().place(x = self.x, y = self.y, width = self.width, height = self.height, anchor = self.anchor)