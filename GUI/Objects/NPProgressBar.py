from tkinter import Frame, DoubleVar
from typing import Literal
from Customs.NPTheme import NPTheme
from Widgets.NPFrame import NPFrame
from math import ceil

currentTheme = NPTheme.getTheme()

class NPProgressBar:
    
    def __init__(self, master: Frame, x: int, y: int, distance: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str, size: int, default: float, maximum: float) -> None:
        
        # Size variables
        self.size = int(size)
        self.barSize = int(10 * self.size)
        self.barDistance = int(0.5 * distance)
        
        # Location variables
        self.x = int(x)
        self.y = int(y)
        self.distance = int(distance)
        self.width = int(10 * self.size + 2 * distance)
        self.height = int(self.size + 2 * distance)
        
        self.anchor = anchor
        self.background = background
        self._frame = NPFrame(master = master, x = self.x, y = self.y, width = self.width, height = self.height, anchor = self.anchor, background = self.background)
        
        # Value variables
        self.default = default
        self.maximum = maximum
        self._value = DoubleVar(master = self._frame, value = self.default)
        
        # ProgressBar's bars
        self._groundBar = NPFrame(master = self._frame, x = self.distance, y = self.distance, width = self.barSize, height = self.size, anchor = "nw", background = currentTheme["progressBar"]["default"])
        self._groundBar.place()
        
        self._unfilledBar = NPFrame(master = self._frame, x = self.distance + self.barDistance, y = self.distance + self.barDistance, width = self.barSize - 2 * self.barDistance, height = self.size - 2 * self.barDistance, anchor = "nw", background = currentTheme["progressBar"]["unfilled"])
        self._unfilledBar.place()
        
        self._filledBar = NPFrame(master = self._frame, x = self.distance + self.barDistance, y = self.distance + self.barDistance, width = 0, height = self.size - 2 * self.barDistance, anchor = "nw", background = currentTheme["progressBar"]["filled"])
        self._fill()
    
    def _fill(self):
        self._filledBar.width = ceil((self._value.get() / self.maximum) * (self.barSize - 2 * self.barDistance))
        self._filledBar.place()
    
    def place(self):
        self._frame.place()
    
    def place_forget(self):
        self._frame.place_forget()
    
    def destroy(self):
        self._frame.destroy()
        self.__dict__.clear()
    
    def setValue(self, value: float = None):
        if value == None:
            return
        if value < 0:
            value = 0
        elif value > self.maximum:
            value = self.maximum
        if value != self._value.get():
            self._value.set(value)
            self._fill()
                
    def resetValue(self):
        self.setValue(self.default)
    
    def getValue(self):
        return self._value.get()