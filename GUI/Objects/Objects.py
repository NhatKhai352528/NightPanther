from tkinter import Frame

class Objects:
    def __init__(self, master: Frame, x: int, y: int, width: int, height: int, distance: int, anchor: str, background: str) -> None:
        self.master = master
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.distance = int(distance)
        self.anchor = anchor
        self.background = background
        self._frame = Frame(master = self.master, background = self.background, borderwidth = 0, container = False, cursor = "arrow", highlightbackground = self.background, highlightcolor = self.background, highlightthickness = 0, relief = "flat", takefocus = False)
    def place(self):
        self._frame.place(x = self.x, y = self.y, width = self.width, height = self.height, anchor = self.anchor)
    def forget(self):
        self._frame.place_forget()
    def destroy(self):
        self._frame.destroy()
        self.__dict__.clear()