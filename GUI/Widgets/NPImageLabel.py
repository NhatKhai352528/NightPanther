from tkinter import Frame, Label
from typing import Any, Literal
from .NPImage import NPImage
from ..Customs.NPTheme import NPTheme

currentTheme = NPTheme.getTheme()

class NPImageLabel(Label):
    
    def __init__(self, master: Frame, x: int, y: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str = currentTheme["background"]["default"], imageFile: str = None, imageWidth: int = None, imageHeight: int = None):
        
        # Location variables
        self._master = master
        self._x = int(x)
        self._y = int(y)
        
        self._anchor = anchor
        self._background = background
        
        # Image variables
        self._imageFile = imageFile
        self._imageWidth = int(imageWidth) if imageWidth != None else currentTheme["default"]["size"]
        self._imageHeight = int (imageHeight) if imageHeight != None else currentTheme["default"]["size"]
        self._image = NPImage(file = self._imageFile, width = self._imageWidth, height = self._imageHeight)
        
        self._width = int(self._imageWidth)
        self._height = int(self._imageHeight)
        
        super().__init__(master = self._master, activebackground = self._background, activeforeground = None, anchor = "center", background = self._background, bitmap = None, borderwidth = 0, compound = "center", cursor = "arrow", disabledforeground = None, font = None, foreground = None, highlightbackground = self._background, highlightcolor = self._background, highlightthickness = 0, image = self._image, justify = "center", relief = "flat", state = "normal", takefocus = False, text = None, textvariable = None, underline = -1, wraplength = 0)
    
    def place(self):
        super().place(x = self._x, y = self._y, width = self._width, height = self._height, anchor = self._anchor)
    
    def destroy(self):
        super().destroy()
        self.__dict__.clear()
    
    def npset(self, attribute: str, value: Any = None):
        if attribute == "image":
            self._image = NPImage(file = self._imageFile, width = self._imageWidth, height = self._imageHeight)
            super().configure(image = self._image)
        elif attribute == "imageFile":
            self._imageFile = value
            self._image = NPImage(file = self._imageFile, width = self._imageWidth, height = self._imageHeight)
            super().configure(image = self._image)
    
    def npget(self, attribute: str):
        if attribute == "width":
            return self._width
        elif attribute == "height":
            return self._height