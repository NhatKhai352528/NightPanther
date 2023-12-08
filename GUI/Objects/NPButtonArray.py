from tkinter import Frame
from tkinter.font import Font
from typing import Any, Literal
from ..Customs.NPTheme import NPTheme
from ..Widgets.NPFrame import NPFrame
from ..Widgets.NPTextButton import NPTextButton

currentTheme = NPTheme.getTheme()

class NPButtonArray:
    
    def __init__(self, master: Frame, mode: Literal["single", "multiple", "voting"], x: int, y: int, distance: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str, rows: int, columns: int, widthSize: int, heightSize: int, font: Font = currentTheme["font"]["default"], defaults: list[list[Literal["default", "active", "disabled"]]] = None, texts: list[list[str]] = None) -> None:
        
        """
        defaults: matrix of rows x columns Literal
        texts: matrix of rows x columns str
        """
        
        # Mode variables
        self.mode = mode
        
        # Size variables
        self.rows = int(rows)
        self.columns = int(columns)
        self.widthSize = int(widthSize)
        self.heightSize = int(heightSize)
        
        # Location variables
        self.x = int(x)
        self.y = int(y)
        self.distance = int(distance)
        self.width = int(self.columns * self.widthSize + (self.columns + 1) * self.distance)
        self.height = int(self.rows * self.heightSize + (self.rows + 1) * self.distance)
        
        self.anchor = anchor
        self.background = background
        self._frame = NPFrame(master = master, x = self.x, y = self.y, width = self.width, height = self.height, anchor = self.anchor, background = self.background)
        
        # Status variables
        self.defaults = [[Literal["default", "active", "disabled"] for _ in range(self.columns)] for _ in range(self.rows)]
        self._status = [[Literal["default", "active", "disabled"] for _ in range(self.columns)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                try:
                    self.defaults[i][j] = defaults[i][j]
                except:
                    self.defaults[i][j] = "default"
        
        # Text variables
        self.texts = [[str for _ in range(self.columns)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                try:
                    self.texts[i][j] = texts[i][j]
                except:
                    self.texts[i][j] = None
        
        # ButtonArray's buttons
        self._buttons = [[Any for _ in range(self.columns)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                self._buttons[i][j] = NPTextButton(master = self._frame, mode = "select", x = j * self.widthSize + (j + 1) * self.distance, y = i * self.heightSize + (i + 1) * self.distance, width = self.widthSize, height = self.heightSize, anchor = "nw", command = None, font = font, repeat = False, state = "normal", text = self.texts[i][j])
                self._setStatus(row = i, column = j, status = self.defaults[i][j])
                if self.mode == "single":
                    self._buttons[i][j].configure(command = lambda event = None, i = i, j = j: self._single(row = i, column = j))
                elif self.mode == "multiple":
                    self._buttons[i][j].configure(command = lambda event = None, i = i, j = j: self._multiple(row = i, column = j))
                elif self.mode == "voting":
                    self._buttons[i][j].configure(command = lambda event = None, i = i, j = j: self._voting(row = i, column = j))
                self._buttons[i][j].place()
    
    def _setStatus(self, row: int, column: int, status: Literal["default", "active", "disabled"]):
        if self._status[row][column] == "disabled":
            return
        if status == self._status[row][column]:
            return
        if status == "disabled":
            self._buttons[row][column].configure(background = self._buttons[row][column].disabledbackground)
            self._buttons[row][column].configure(state = "disabled")
        elif status == "default":
            self._buttons[row][column].configure(activebackground = self._buttons[row][column].activebackground)
            self._buttons[row][column].configure(background = self._buttons[row][column].background)
        elif status == "active":
            self._buttons[row][column].configure(activebackground = self._buttons[row][column].background)
            self._buttons[row][column].configure(background = self._buttons[row][column].activebackground)
        self._status[row][column] = status
    
    def _single(self, row: int, column: int):
        for i in range(self.rows):
            for j in range(self.columns):
                if i == row and j == column:
                    self._setStatus(row = i, column = j, status = "active")
                else:
                    self._setStatus(row = i, column = j, status = "default")
    
    def _multiple(self, row: int, column: int):
        if self._status[row][column] == "active":
            self._setStatus(row = row, column = column, status = "default")
        elif self._status[row][column] == "default":
            self._setStatus(row = row, column = column, status = "active")
    
    def _voting(self, row: int, column: int):
        for i in range(self.rows):
            for j in range(self.columns):
                if i <= row and j <= column:
                    self._setStatus(row = i, column = j, status = "active")
                else:
                    self._setStatus(row = i, column = j, status = "default")
    
    def place(self):
        self._frame.place()
    
    def place_forget(self):
        self._frame.place_forget()
    
    def destroy(self):
        self._frame.destroy()
        self.__dict__.clear()
    
    def isDefault(self, row: int, column: int):
        return self._status[row][column] == "default"
    
    def isActive(self, row: int, column: int):
        return self._status[row][column] == "active"
    
    def isDisabled(self, row: int, column: int):
        return self._status[row][column] == "disabled"