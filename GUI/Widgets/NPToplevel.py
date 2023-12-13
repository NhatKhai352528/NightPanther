from tkinter import Tk, Toplevel

class NPToplevel(Toplevel):
    
    def __init__(self, master: Tk, x: int, y: int, width: int, height: int, background: str) -> None:
        
        self._master = master
        self._x = int(x)
        self._y = int(y)
        self._width = int(width)
        self._height = int(height)
        self._background = background
        
        super().__init__(master = self._master, background = self._background, borderwidth = 0, container = False, cursor = "arrow", highlightbackground = self._background, highlightcolor = self._background, highlightthickness = 0, relief = "flat", takefocus = False)
        super().geometry(str(self._width) + "x" + str(self._height) + "+" + str(self._x) + "+" + str(self._y))
        
        # super().overrideredirect(boolean = True)