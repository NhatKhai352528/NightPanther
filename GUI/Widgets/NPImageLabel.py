from tkinter import Frame, Label
from typing import Literal
from Customs.NPTheme import NPTheme
from Widgets.NPImage import NPImage
from Customs.NPTheme import NPTheme

currentTheme = NPTheme.getTheme()

class NPImageLabel(Label):
    
    def __init__(self, master: Frame, x: int, y: int, width: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str = currentTheme["background"]["default"], imageFile: str = None, imageWidth: int = None, imageHeight: int = None) -> None:
        
        # Location variables
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.anchor = anchor
        
        # Image variables
        self.imageFile = imageFile
        self.imageWidth = int(imageWidth) if imageWidth != None else currentTheme["default"]["size"]
        self.imageHeight = int (imageHeight) if imageHeight != None else currentTheme["default"]["size"]
        self.image = NPImage(file = self.imageFile, width = self.imageWidth, height = self.imageHeight)
        
        super().__init__(master, activebackground = background, activeforeground = None, anchor = "center", background = background, bitmap = None, borderwidth = 0, compound = "center", cursor = "arrow", disabledforeground = None, font = None, foreground = None, highlightbackground = background, highlightcolor = background, highlightthickness = 0, image = self.image.image, justify = "center", relief = "flat", state = "normal", takefocus = False, text = None, textvariable = None, underline = -1, wraplength = 0)
    
    def place(self):
        super().place(x = self.x, y = self.y, width = self.width, anchor = self.anchor)
        
    def getHeight(self):
        return super().winfo_reqheight()