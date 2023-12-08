from tkinter import Frame, StringVar
from tkinter.font import Font
from typing import Any, Literal
from ..Customs.NPLanguage import NPLanguage
from ..Customs.NPTheme import NPTheme
from ..Widgets.NPEntry import NPEntry
from ..Widgets.NPFrame import NPFrame
from ..Widgets.NPTextButton import NPTextButton

currentTheme = NPTheme.getTheme()
currentLanguage = NPLanguage.getLanguage()

class NPKeyBoard:
    
    def __init__(self, master: Frame, x: int, y: int, distance: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str, size: int, default: str, maximum: int, show: str, entryFont: Font = currentTheme["font"]["default"], inputFont: Font = currentTheme["font"]["default"], actionFont: Font = currentTheme["font"]["default"], inputTexts: list[str] = None, actionTexts: list[str] = None, actionCommands: list[Any] = None) -> None:
        
        """
        inputTexts: list of 2 str
        actionTexts: list of 2 str
        actionCommands: list of 2 Any
        """
        
        # Size variables
        self.rows = 4
        self.columns = 4
        self.size = int(size)
        self.actionSize = int(2 * self.size)
        
        # Location variables
        self.x = int(x)
        self.y = int(y)
        self.distance = int(distance)
        self.width = int((self.columns - 1) * self.size + 1 * self.actionSize + (self.columns + 1) * self.distance)
        self.height = int((self.rows + 1.5) * self.size + (self.rows + 2) * self.distance)
        
        self.anchor = anchor
        self.background = background
        self._frame = NPFrame(master = master, x = self.x, y = self.y, width = self.width, height = self.height, anchor = self.anchor, background = self.background)
        
        # Value variables
        self.default = default
        self.maximum = int(maximum)
        self.show = show
        self._value = StringVar(master = self._frame, value = self.default)
        
        # Font variables
        self.entryFont = entryFont
        self.inputFont = inputFont
        self.actionFont = actionFont
        
        # Input variables
        self._inputTexts = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", None]]
        try:
            self._inputTexts[3][0] = inputTexts[0]
        except:
            self._inputTexts[3][0] = None
        try:
            self._inputTexts[3][2] = inputTexts[1]
        except:
            self._inputTexts[3][2] = None
        
        self._inputCommands = [[Any for _ in range(self.columns - 1)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns - 1):
                self._inputCommands[i][j] = lambda event = None, i = i, j = j: self._insert(self._inputTexts[i][j])
        
        # Action variables
        self._actionTexts = [currentLanguage["keyBoard"]["clear"], currentLanguage["keyBoard"]["delete"], None, None]
        try:
            self._actionTexts[2] = actionTexts[0]
        except:
            self._actionTexts[2] = None
        try:
            self._actionTexts[3] = actionTexts[1]
        except:
            self._actionTexts[3] = None
            
        self._actionCommands = [lambda event = None: self._clear(), lambda event = None: self._delete(), None, None]
        try:
            self._actionCommands[2] = actionCommands[0]
        except:
            self._actionCommands[2] = None
        try:
            self._actionCommands[3] = actionCommands[1]
        except:
            self._actionCommands[3] = None
        
        # KeyBoard's screen
        self._entry = NPEntry(master = self._frame, x = self.distance, y = self.distance, width = self.width - 2 * self.distance, height = 1.5 * self.size, anchor = "nw", font = self.entryFont, invalidcommand = None, show = self.show, state = "readonly", validate = "none", validatecommand = None, textvariable = self._value)
        self._entry.place()
        
        # KeyBoard's input buttons
        self._inputButtons = [[Any for _ in range(self.columns - 1)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns - 1):
                self._inputButtons[i][j] = NPTextButton(master = self._frame, mode = "input", x = j * self.size + (j + 1) * self.distance, y = (i + 1.5) * self.size + (i + 2) * self.distance, width = self.size, height = self.size, anchor = "nw", command = self._inputCommands[i][j], font = self.inputFont, repeat = False, state = "normal" if self._inputTexts[i][j] != None else "disabled", text = self._inputTexts[i][j])
                self._inputButtons[i][j].place()
        
        # KeyBoard's action buttons
        self._actionButtons = [Any for _ in range(self.rows)]
        for i in range(self.rows):
            self._actionButtons[i] = NPTextButton(master = self._frame, mode = "action", x = self.width - self.distance, y = (i + 1.5) * self.size + (i + 2) * self.distance, width = self.actionSize, height = self.size, anchor = "ne", command = self._actionCommands[i], font = self.actionFont, repeat = False, state = "normal" if self._actionTexts[i] != None else "disabled", text = self._actionTexts[i])
            self._actionButtons[i].place()
    
    def _insert(self, text: str):
        if self._value.get() == self.default:
            self._value.set("")
        if len(self._value.get()) < self.maximum:
            self._value.set(self._value.get() + text[0])
    
    def _clear(self):
        self._value.set(self.default)
    
    def _delete(self):
        if self._value.get() == self.default:
            return
        if len(self._value.get()) != 0:
            self._value.set(self._value.get()[:-1])
        if len(self._value.get()) == 0:
            self._value.set(self.default)
    
    def place(self):
        self._frame.place()
    
    def place_forget(self):
        self._frame.place_forget()
    
    def destroy(self):
        self._frame.destroy()
        self.__dict__.clear()
    
    def resetValue(self):
        self._value.set(self.default)
    
    def getValue(self):
        return self._value.get()