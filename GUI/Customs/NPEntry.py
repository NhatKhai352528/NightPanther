from tkinter import Entry, Frame, Variable
from tkinter.font import Font
from typing import Any, Literal
from Customs.NPTheme import NPTheme

currentTheme = NPTheme.getTheme()

class NPEntry(Entry):
    
    def __init__(self, master: Frame, x: int, y: int, width: int, height: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], font: Font = currentTheme["font"]["normal"], invalidcommand: Any = None, show: str = "", state: Literal["normal", "disabled", "readonly"] = "normal", validate: Literal["none", "focus", "focusin", "focusout", "key", "all"] = "none", validatecommand: Any = None, textvariable: Variable = None) -> None:
        
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.anchor = anchor
        
        self.foreground = currentTheme["foreground"]["default"]
        self.background = currentTheme["entry"]["default"]
        self.selectbackground = currentTheme["entry"]["select"]
        self.disabledbackground = currentTheme["entry"]["disabled"]
        
        super().__init__(master = master, background = self.background, borderwidth = 0, cursor = "xterm", disabledbackground = self.disabledbackground, disabledforeground = self.foreground, exportselection = False, font = font, foreground = self.foreground, highlightbackground = self.background, highlightcolor = self.background, highlightthickness = 0, insertbackground = self.foreground, insertborderwidth = 0, insertofftime = 1000, insertontime = 1000, insertwidth = 1, invalidcommand = invalidcommand, justify = "center", readonlybackground = self.background, relief = "flat", selectbackground = self.selectbackground, selectborderwidth = 0, selectforeground = self.foreground, show = show, state = state, takefocus = False, textvariable = textvariable, validate = validate, validatecommand = validatecommand)
    
    def place(self):
        super().place(x = self.x, y = self.y, width = self.width, height = self.height, anchor = self.anchor)