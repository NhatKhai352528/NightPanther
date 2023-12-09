from tkinter import Frame, StringVar
from tkinter.font import Font
from typing import Any, Literal
from .NPObjects import NPObjects
from ..Customs.NPLanguage import NPLanguage
from ..Customs.NPTheme import NPTheme
from ..Widgets.NPEntry import NPEntry
from ..Widgets.NPTextButton import NPTextButton

currentTheme = NPTheme.getTheme()
currentLanguage = NPLanguage.getLanguage()

class NPKeyBoard(NPObjects):
    
    def __init__(self, master: Frame, x: int, y: int, distance: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str, size: int, default: str, maximum: int, show: str, entryFont: Font = currentTheme["font"]["default"], inputFont: Font = currentTheme["font"]["default"], actionFont: Font = currentTheme["font"]["default"], inputTexts: list[str] = None, actionTexts: list[str] = None, actionCommands: list[Any] = None):
        
        """
        inputTexts: list of 2 str
        actionTexts: list of 2 str
        actionCommands: list of 2 Any
        """
        
        # Size variables
        self._rows = 4
        self._columns = 4
        self._size = int(size)
        self._actionSize = int(2 * self._size)
        
        # Invoking parent's __init__ function
        width = (self._columns - 1) * self._size + 1 * self._actionSize + (self._columns + 1) * distance
        height = (self._rows + 1.5) * self._size + (self._rows + 2) * distance
        super().__init__(master = master, x = x, y = y, width = width, height = height, distance = distance, anchor = anchor, background = background)
        
        # Value variables
        self._default = default
        self._maximum = int(maximum)
        self._show = show
        self._value = StringVar(master = self._frame, value = self._default)
        
        # Font variables
        self._entryFont = entryFont
        self._inputFont = inputFont
        self._actionFont = actionFont
        
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
        
        self._inputCommands = [[Any for _ in range(self._columns - 1)] for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(self._columns - 1):
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
        self._entry = NPEntry(master = self._frame, x = self._distance, y = self._distance, width = self._width - 2 * self._distance, height = 1.5 * self._size, anchor = "nw", font = self._entryFont, invalidcommand = None, show = self._show, state = "readonly", validate = "none", validatecommand = None, textvariable = self._value)
        self._entry.place()
        
        # KeyBoard's input buttons
        self._inputButtons = [[Any for _ in range(self._columns - 1)] for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(self._columns - 1):
                self._inputButtons[i][j] = NPTextButton(master = self._frame, mode = "input", x = j * self._size + (j + 1) * self._distance, y = (i + 1.5) * self._size + (i + 2) * self._distance, width = self._size, height = self._size, anchor = "nw", command = self._inputCommands[i][j], font = self._inputFont, repeat = False, state = "normal" if self._inputTexts[i][j] != None else "disabled", text = self._inputTexts[i][j])
                self._inputButtons[i][j].place()
        
        # KeyBoard's action buttons
        self._actionButtons = [Any for _ in range(self._rows)]
        for i in range(self._rows):
            self._actionButtons[i] = NPTextButton(master = self._frame, mode = "action", x = self._width - self._distance, y = (i + 1.5) * self._size + (i + 2) * self._distance, width = self._actionSize, height = self._size, anchor = "ne", command = self._actionCommands[i], font = self._actionFont, repeat = False, state = "normal" if self._actionTexts[i] != None else "disabled", text = self._actionTexts[i])
            self._actionButtons[i].place()
    
    def _insert(self, text: str):
        if self._value.get() == self._default:
            self._value.set("")
        if len(self._value.get()) < self._maximum:
            self._value.set(self._value.get() + text[0])
    
    def _clear(self):
        self._value.set(self._default)
    
    def _delete(self):
        if self._value.get() == self._default:
            return
        if len(self._value.get()) != 0:
            self._value.set(self._value.get()[:-1])
        if len(self._value.get()) == 0:
            self._value.set(self._default)
    
    def resetValue(self):
        self._value.set(self._default)
    
    def getValue(self):
        return self._value.get()