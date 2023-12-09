from tkinter import Entry, Frame, Variable
from tkinter.font import Font
from typing import Any, Literal
from ..Customs.NPTheme import NPTheme

currentTheme = NPTheme.getTheme()

class NPEntry(Entry):
    
    def __init__(self, master: Frame, x: int, y: int, width: int, height: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], font: Font = currentTheme["font"]["default"], invalidcommand: Any = None, show: str = "", state: Literal["normal", "disabled", "readonly"] = "normal", validate: Literal["none", "focus", "focusin", "focusout", "key", "all"] = "none", validatecommand: Any = None, textvariable: Variable = None):
        
        # Location variables
        self._master = master
        self._x = int(x)
        self._y = int(y)
        self._width = int(width)
        self._height = int(height)
        self._anchor = anchor
        
        # Value variables
        self._show = show
        self._state = state
        self._textvariable = textvariable
        
        # Theme variables
        self._font = font
        self._foreground = currentTheme["foreground"]["default"]
        self._background = currentTheme["entry"]["default"]
        self._selectbackground = currentTheme["entry"]["select"]
        self._disabledbackground = currentTheme["entry"]["disabled"]
        
        # Unused variables
        self._invalidcommand = invalidcommand
        self._validate = validate
        self._validatecommand = validatecommand
        
        super().__init__(master = self._master, background = self._background, borderwidth = 0, cursor = "xterm", disabledbackground = self._disabledbackground, disabledforeground = self._foreground, exportselection = False, font = self._font, foreground = self._foreground, highlightbackground = self._background, highlightcolor = self._background, highlightthickness = 0, insertbackground = self._foreground, insertborderwidth = 0, insertofftime = 1000, insertontime = 1000, insertwidth = 1, invalidcommand = self._invalidcommand, justify = "center", readonlybackground = self._background, relief = "flat", selectbackground = self._selectbackground, selectborderwidth = 0, selectforeground = self._foreground, show = self._show, state = self._state, takefocus = False, textvariable = self._textvariable, validate = self._validate, validatecommand = self._validatecommand)
    
    def place(self):
        super().place(x = self._x, y = self._y, width = self._width, height = self._height, anchor = self._anchor)
    
    def destroy(self):
        super().destroy()
        self.__dict__.clear()