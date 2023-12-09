from tkinter import Frame, DoubleVar
from tkinter.font import Font
from typing import Any, Literal
from .NPObjects import NPObjects
from ..Customs.NPTheme import NPTheme
from ..Widgets.NPEntry import NPEntry
from ..Widgets.NPTextButton import NPTextButton

currentTheme = NPTheme.getTheme()

def maxDecimal(nums: list[float]):
    maxDecimal = 0
    for num in nums:
        if "." in str(num):
            strDecimal = str(num).split(".")[1]
            if strDecimal != "0":
                maxDecimal = max(maxDecimal, len(strDecimal))
    return maxDecimal

def roundFloat(num: float, decimal: int):
    if decimal == 0:
        return int(num)
    return round(num, decimal)

class NPSpinBox(NPObjects):
    
    def __init__(self, master: Frame, x: int, y: int, distance: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str, size: int, default: float, minimum: float, maximum: float, step: float, wrap: bool, entryFont: Font = currentTheme["font"]["default"], inputFont: Font = currentTheme["font"]["default"], actionFont: Font = currentTheme["font"]["default"], actionText: str = None, actionCommand: Any = None):
        
        # Size variables
        self._size = int(size)
        self._entrySize = int(3 * self._size)
        self._actionSize = int(2 * self._size)
        
        # Invoking parent's __init__ function
        width = 2 * self._size + 1 * self._entrySize + 1 * self._actionSize + 5 * distance
        height = self._size + 2 * distance
        super().__init__(master = master, x = x, y = y, width = width, height = height, distance = distance, anchor = anchor, background = background)
        
        # Value variables
        self._default = float(default)
        self._minimum = float(minimum)
        self._maximum = float(maximum)
        self._step = float(step)
        
        self._wrap = wrap
        self._decimal = maxDecimal(nums = [self._default, self._minimum, self._maximum, self._step])
        self._value = DoubleVar(master = self._frame, value = roundFloat(self._default, self._decimal))
        
        # Font variables
        self._entryFont = entryFont
        self._inputFont = inputFont
        self._actionFont = actionFont
        
        # Action variables
        self._actionText = actionText
        self._actionCommand = actionCommand
        
        # SpinBox's screen
        self._entry = NPEntry(master = self._frame, x = self._size + 2 * self._distance, y = self._distance, width = self._entrySize, height = self._size, anchor = "nw", font = self._entryFont, invalidcommand = None, show = "", state = "readonly", validate = "none", validatecommand = None, textvariable = self._value)
        self._entry.place()
        
        # SpinBox's decrease button
        self._decreaseButton = NPTextButton(master = self._frame, mode = "input", x = self._distance, y = self._distance, width = self._size, height = self._size, anchor = "nw", command = lambda event = None: self._decrease(), font = self._inputFont, repeat = True, state = "normal", text = "-")
        self._decreaseButton.place()
        
        # SpinBox's increase button
        self._increaseButton = NPTextButton(master = self._frame, mode = "input", x = self._size + self._entrySize + 3 * self._distance, y = self._distance, width = self._size, height = self._size, anchor = "nw", command = lambda event = None: self._increase(), font = self._inputFont, repeat = True, state = "normal", text = "+")
        self._increaseButton.place()
        
        # SpinBox's action button
        self._actionButton = NPTextButton(master = self._frame, mode = "action", x = self._width - self._distance, y = self._distance, width = self._actionSize, height = self._size, anchor = "ne", command = self._actionCommand, font = self._actionFont, repeat = False, state = "normal" if self._actionText != None else "disabled", text = self._actionText)
        self._actionButton.place()
        
    def _decrease(self):
        value = roundFloat(self._value.get(), self._decimal)
        if value - self._step >= self._minimum:
            self._value.set(roundFloat(value - self._step, self._decimal))
        elif self._wrap == True and value == self._minimum:
            self._value.set(roundFloat(self._maximum, self._decimal))
        else:
            self._value.set(roundFloat(self._minimum, self._decimal))
    
    def _increase(self):
        value = roundFloat(self._value.get(), self._decimal)
        if value + self._step <= self._maximum:
            self._value.set(roundFloat(value + self._step, self._decimal))
        elif self._wrap == True and value == self._maximum:
            self._value.set(roundFloat(self._minimum, self._decimal))
        else:
            self._value.set(roundFloat(self._maximum, self._decimal))
    
    def resetValue(self):
        self._value.set(roundFloat(self._default, self._decimal, self._decimal))
    
    def getValue(self):
        return roundFloat(self._value.get(), self._decimal)
        