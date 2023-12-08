from tkinter import Frame, DoubleVar
from tkinter.font import Font
from typing import Any, Literal
from ..Customs.NPTheme import NPTheme
from ..Widgets.NPEntry import NPEntry
from ..Widgets.NPFrame import NPFrame
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

class NPSpinBox:
    
    def __init__(self, master: Frame, x: int, y: int, distance: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str, size: int, default: float, minimum: float, maximum: float, step: float, wrap: bool, entryFont: Font = currentTheme["font"]["default"], inputFont: Font = currentTheme["font"]["default"], actionFont: Font = currentTheme["font"]["default"], actionText: str = None, actionCommand: Any = None) -> None:
        
        # Size variables
        self.size = int(size)
        self.entrySize = int(3 * self.size)
        self.actionSize = int(2 * self.size)
        
        # Location variables
        self.x = int(x)
        self.y = int(y)
        self.distance = int(distance)
        self.width = int(2 * self.size + 1 * self.entrySize + 1 * self.actionSize + 5 * self.distance)
        self.height = int(self.size + 2 * self.distance)
        
        self.anchor = anchor
        self.background = background
        self._frame = NPFrame(master = master, x = self.x, y = self.y, width = self.width, height = self.height, anchor = self.anchor, background = self.background)
        
        # Value variables
        self.default = float(default)
        self.minimum = float(minimum)
        self.maximum = float(maximum)
        self.step = float(step)
        
        self.wrap = wrap
        self.decimal = maxDecimal(nums = [self.default, self.minimum, self.maximum, self.step])
        self._value = DoubleVar(master = master, value = roundFloat(self.default, self.decimal))
        
        # Font variables
        self.entryFont = entryFont
        self.inputFont = inputFont
        self.actionFont = actionFont
        
        # Action variables
        self.actionText = actionText
        self.actionCommand = actionCommand
        
        # SpinBox's screen
        self._entry = NPEntry(master = self._frame, x = self.size + 2 * self.distance, y = self.distance, width = self.entrySize, height = self.size, anchor = "nw", font = self.entryFont, invalidcommand = None, show = "", state = "readonly", validate = "none", validatecommand = None, textvariable = self._value)
        self._entry.place()
        
        # SpinBox's decrease button
        self._decreaseButton = NPTextButton(master = self._frame, mode = "input", x = self.distance, y = self.distance, width = self.size, height = self.size, anchor = "nw", command = lambda event = None: self._decrease(), font = self.inputFont, repeat = True, state = "normal", text = "-")
        self._decreaseButton.place()
        
        # SpinBox's increase button
        self._increaseButton = NPTextButton(master = self._frame, mode = "input", x = self.size + self.entrySize + 3 * self.distance, y = self.distance, width = self.size, height = self.size, anchor = "nw", command = lambda event = None: self._increase(), font = self.inputFont, repeat = True, state = "normal", text = "+")
        self._increaseButton.place()
        
        # SpinBox's action button
        self._actionButton = NPTextButton(master = self._frame, mode = "action", x = self.width - self.distance, y = self.distance, width = self.actionSize, height = self.size, anchor = "ne", command = self.actionCommand, font = self.actionFont, repeat = False, state = "normal" if self.actionText != None else "disabled", text = self.actionText)
        self._actionButton.place()
        
    def _decrease(self):
        value = roundFloat(self._value.get(), self.decimal)
        if value - self.step >= self.minimum:
            self._value.set(value - self.step)
        elif self.wrap == True and value == self.minimum:
            self._value.set(self.maximum)
        else:
            self._value.set(self.minimum)
    
    def _increase(self):
        value = roundFloat(self._value.get(), self.decimal)
        if value + self.step <= self.maximum:
            self._value.set(value + self.step)
        elif self.wrap == True and value == self.maximum:
            self._value.set(self.minimum)
        else:
            self._value.set(self.maximum)
    
    def place(self):
        self._frame.place()
    
    def place_forget(self):
        self._frame.place_forget()
    
    def destroy(self):
        self._frame.destroy()
        self.__dict__.clear()
    
    def resetValue(self):
        self._value.set(roundFloat(self.default, self.decimal))
    
    def getValue(self):
        return self._value.get()
        