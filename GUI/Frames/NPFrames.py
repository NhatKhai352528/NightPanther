from tkinter import Frame, Tk
from typing import Literal, Union
from ..Widgets.NPFrame import NPFrame

class NPFrames:
    
    def __init__(self, master: Union[Frame, Tk], x: int, y: int, width: int, height: int, distance: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str):
        
        # Location variables
        self._master = master
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._distance = distance
        
        self._anchor = anchor
        self._background = background
        self._frame = NPFrame(master = self._master, x = self._x, y = self._y, width = self._width, height = self._height, anchor = self._anchor, background = self._background)
        
        # Frame's items
        self._items = []
        
    def place(self):
        self._frame.place()
    
    def place_forget(self):
        self._frame.place_forget()
    
    def destroy(self):
        self._frame.destroy()
        self.__dict__.clear()
    
    def npget(self, attribute: str):
        if attribute == "master":
            return self._master
        elif attribute == "frame":
            return self._frame
        elif attribute == "x":
            return self._x
        elif attribute == "y":
            return self._y
        elif attribute == "width":
            return self._width
        elif attribute == "height":
            return self._height
        elif attribute == "distance":
            return self._distance
        elif attribute == "anchor":
            return self._anchor
        elif attribute == "background":
            return self._background