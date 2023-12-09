from tkinter import Frame, DoubleVar
from typing import Literal
from .NPObjects import NPObjects
from ..Customs.NPTheme import NPTheme
from ..Widgets.NPFrame import NPFrame

currentTheme = NPTheme.getTheme()

class NPProgressBar(NPObjects):
    
    def __init__(self, master: Frame, x: int, y: int, distance: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str, size: int, default: float, maximum: float):
        
        # Size variables
        self._size = int(size)
        self._barSize = int(10 * self._size)
        self._barDistance = int(0.5 * distance)
        
        # Invoking parent's __init__ function
        width = self._barSize + 2 * distance
        height = self._size + 2 * distance
        super().__init__(master = master, x = x, y = y, width = width, height = height, distance = distance, anchor = anchor, background = background)
        
        # Value variables
        self._default = default
        self._maximum = maximum
        self._value = DoubleVar(master = self._frame, value = self._default)
        
        # ProgressBar's bars
        self._groundBar = NPFrame(master = self._frame, x = self._distance, y = self._distance, width = self._barSize, height = self._size, anchor = "nw", background = currentTheme["progressBar"]["default"])
        self._groundBar.place()
        
        self._unfilledBar = NPFrame(master = self._frame, x = self._distance + self._barDistance, y = self._distance + self._barDistance, width = self._barSize - 2 * self._barDistance, height = self._size - 2 * self._barDistance, anchor = "nw", background = currentTheme["progressBar"]["unfilled"])
        self._unfilledBar.place()
        
        self._filledBar = NPFrame(master = self._frame, x = self._distance + self._barDistance, y = self._distance + self._barDistance, width = 0, height = self._size - 2 * self._barDistance, anchor = "nw", background = currentTheme["progressBar"]["filled"])
        self._fill()
    
    def _fill(self):
        if self._maximum != 0:
            self._filledBar.npset("width", int((self._value.get() / self._maximum) * (self._barSize - 2 * self._barDistance)))
        else:
            self._filledBar.npset("width", int(self._barSize - 2 * self._barDistance))
        self._filledBar.place()
    
    def setValue(self, value: float = None):
        if value == None:
            return
        if value < 0:
            value = 0
        elif value > self._maximum:
            value = self._maximum
        if value != self._value.get():
            self._value.set(value)
            self._fill()
                
    def resetValue(self):
        self._setValue(self._default)
    
    def getValue(self):
        return self._value.get()