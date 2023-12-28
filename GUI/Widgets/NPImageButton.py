from tkinter import Button, Frame
from typing import Any, Literal
from .NPImage import NPImage
from ..Customs.NPTheme import NPTheme

class NPImageButton(Button):
    
    def __init__(self, master: Frame, mode: Literal["input", "action", "select"], x: int, y: int, width: int, height: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], command: Any = None, imageFile: str = None, repeat: bool = False, state: Literal["normal", "disabled"] = "normal"):

        self._currentTheme = NPTheme.getTheme()
        
        # Mode variables
        self._mode = mode
        
        # Location variables
        self._master = master
        self._x = int(x)
        self._y = int(y)
        self._width = int(width)
        self._height = int(height)
        self._anchor = anchor
        
        # Action variables
        self._command = command
        self._repeat = repeat
        self._state = state
        
        # Image variables
        self._imageFile = imageFile
        self._image = NPImage(file = self._imageFile, width = 0.8 * self._width, height = 0.8 * self._height)
        
        # Theme variables
        self._background = self._currentTheme["button"][self._mode]["default"]
        self._activebackground = self._currentTheme["button"][self._mode]["active"]
        self._disabledbackground = self._currentTheme["button"][self._mode]["disabled"]
        
        super().__init__(master = self._master, activebackground = self._activebackground, activeforeground = None, anchor = "center", background = self._background if self._state == "normal" else self._disabledbackground, bitmap = None, borderwidth = 0, command = self._command, compound = "center", cursor = "arrow", default = "normal", disabledforeground = None, font = None, foreground = None, highlightbackground = self._background, highlightcolor = self._background, highlightthickness = 0, image = self._image, justify = "center", overrelief = "flat", relief = "flat", repeatdelay = 1000, repeatinterval = 0 if self._repeat == False else 10, state = self._state, takefocus = False, text = None, textvariable = None, underline = -1, wraplength = 0)
    
    def place(self):
        super().place(x = self._x, y = self._y, width = self._width, height = self._height, anchor = self._anchor)
    
    def destroy(self):
        super().destroy()
        self.__dict__.clear()
    
    def npset(self, attribute: str, value: Any = None):
        if attribute == "command":
            self._command = value
            super().configure(command = self._command)
        elif attribute == "state":
            self._state = value
            super().configure(background = self._background if self._state == "normal" else self._disabledbackground)
            super().configure(state = self._state)
        elif attribute == "imageFile":
            self._imageFile = value
            self._image = NPImage(file = self._imageFile, width = 0.8 * self._width, height = 0.8 * self._height)
            super().configure(image = self._image)
    
    def npget(self, attribute: str):
        if attribute == "background":
            return self._background
        elif attribute == "activebackground":
            return self._activebackground
        elif attribute == "disabledbackground":
            return self._disabledbackground
