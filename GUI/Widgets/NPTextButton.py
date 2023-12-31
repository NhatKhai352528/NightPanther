from tkinter import Button, Frame
from tkinter.font import Font
from typing import Any, Literal
from ..Customs.NPTheme import NPTheme

defaultTheme = NPTheme.getTheme()
        
class NPTextButton(Button):
    
    def __init__(self, master: Frame, mode: Literal["input", "action", "select"], x: int, y: int, width: int, height: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], command: Any = None, font: Font = defaultTheme["font"]["default"], repeat: bool = False, state: Literal["normal", "disabled"] = "normal", text: str = None):

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
        
        # Theme variables
        self._foreground = self._currentTheme["foreground"]["inverse"]
        self._background = self._currentTheme["button"][self._mode]["default"]
        self._activebackground = self._currentTheme["button"][self._mode]["active"]
        self._disabledbackground = self._currentTheme["button"][self._mode]["disabled"]
        
        # Text variables
        self._font = font
        self._text = text
        
        super().__init__(master = self._master, activebackground = self._activebackground, activeforeground = self._foreground, anchor = "center", background = self._background if self._state == "normal" else self._disabledbackground, bitmap = None, borderwidth = 0, command = self._command, compound = "center", cursor = "arrow", default = "normal", disabledforeground = self._foreground, font = self._font, foreground = self._foreground, highlightbackground = self._background, highlightcolor = self._background, highlightthickness = 0, image = None, justify = "center", overrelief = "flat", relief = "flat", repeatdelay = 1000, repeatinterval = 0 if self._repeat == False else 10, state = self._state, takefocus = False, text = self._text, textvariable = None, underline = -1, wraplength = 0)
        
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
    
    def npget(self, attribute: str):
        if attribute == "background":
            return self._background
        elif attribute == "activebackground":
            return self._activebackground
        elif attribute == "disabledbackground":
            return self._disabledbackground
        elif attribute == "height":
            return self._height