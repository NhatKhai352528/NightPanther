from tkinter import Frame, StringVar
from tkinter.font import Font
from typing import Any, Literal
from Objects.Objects import Objects
from Customs.NPEntry import NPEntry
from Customs.NPTextButton import NPTextButton
from Customs.NPTheme import NPTheme

currentTheme = NPTheme.getTheme()

class KeyBoard(Objects):
    
    def __init__(self, master: Frame, x: int, y: int, distance: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str, size: int, default: str, maximum: int, show: str, entryFont: Font = currentTheme["font"]["normal"], inputFont: Font = currentTheme["font"]["normal"], actionFont: Font = currentTheme["font"]["normal"], inputTexts: list[str, str] = None, actionTexts: list[str, str] = None, actionCommands: list[Any, Any] = None) -> None:
        
        # Predefined variables
        self.rows = 4
        self.columns = 4
        
        # Size variables
        self.size = int(size)
        self.actionSize = 2 * self.size
        
        # Location variables
        width = (self.columns - 1) * self.size + 1 * self.actionSize + (self.columns + 1) * distance
        height = (self.rows + 1.5) * self.size + (self.rows + 2) * distance
        
        # Invoking parent __init__
        super().__init__(master, x, y, width, height, distance, anchor, background)
        
        # Value variables
        self.default = default
        self.maximum = maximum
        self.show = show
        
        # Font variables
        self.entryFont = entryFont
        self.inputFont = inputFont
        self.actionFont = actionFont
        
        # Input variables
        self._inputTexts = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", None]]
        if inputTexts != None:
            self._inputTexts[3][0] = inputTexts[0]
            self._inputTexts[3][2] = inputTexts[1]
        
        self._inputCommands = [[Any for _ in range(self.columns - 1)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns - 1):
                self._inputCommands[i][j] = lambda event = None, i = i, j = j: self._insert(self._inputTexts[i][j])
        
        # Action variables
        self._actionCommands = [lambda event = None: self._clear(), lambda event = None: self._delete(), None, None]
        if actionCommands != None:
            self._actionCommands[2] = actionCommands[0]
            self._actionCommands[3] = actionCommands[1]
        
        self._actionTexts = ["Clear", "Delete", None, None]
        if actionTexts != None:
            self._actionTexts[2] = actionTexts[0]
            self._actionTexts[3] = actionTexts[1]
        
        # KeyBoard's screen
        self._value = StringVar(master = self._frame, value = self.default)
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
        if self._value.get() != self.default:
            if len(self._value.get()) != 0:
                self._value.set(self._value.get()[:-1])
            if len(self._value.get()) == 0:
                self._value.set(self.default)