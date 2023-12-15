from tkinter import Frame
from tkinter.font import Font
from typing import Any, Literal
from .NPObjects import NPObjects
from ..Customs.NPTheme import NPTheme
from ..Widgets.NPTextButton import NPTextButton

currentTheme = NPTheme.getTheme()

class NPButtonArray(NPObjects):
    
    def __init__(self, master: Frame, mode: Literal["single", "multiple"], x: int, y: int, distance: int, anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"], background: str, rows: int, columns: int, widthSize: int, heightSize: int, font: Font = currentTheme["font"]["default"], defaults: list[list[Literal["default", "active", "disabled"]]] = None, texts: list[list[str]] = None):
        
        # Mode variables
        self._mode = mode
        
        # Size variables
        self._rows = int(rows)
        self._columns = int(columns)
        self._widthSize = int(widthSize)
        self._heightSize = int(heightSize)
        
        # Invoking parent's __init__ function
        width = self._columns * self._widthSize + (self._columns + 1) * distance
        height = self._rows * self._heightSize + (self._rows + 1) * distance
        super().__init__(master = master, x = x, y = y, width = width, height = height, distance = distance, anchor = anchor, background = background)
        
        # Font variables
        self._font = font
        
        # Status variables
        self._defaults = [[Literal["default", "active", "disabled"] for _ in range(self._columns)] for _ in range(self._rows)]
        self._status = [[Literal["default", "active", "disabled"] for _ in range(self._columns)] for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(self._columns):
                try:
                    self._defaults[i][j] = defaults[i][j]
                except:
                    self._defaults[i][j] = "default"
        
        # Text variables
        self._texts = [[str for _ in range(self._columns)] for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(self._columns):
                try:
                    self._texts[i][j] = texts[i][j]
                except:
                    self._texts[i][j] = None
        
        # ButtonArray's buttons
        self._buttons = [[Any for _ in range(self._columns)] for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(self._columns):
                self._buttons[i][j] = NPTextButton(master = self._frame, mode = "select", x = j * self._widthSize + (j + 1) * self._distance, y = i * self._heightSize + (i + 1) * self._distance, width = self._widthSize, height = self._heightSize, anchor = "nw", command = None, font = self._font, repeat = False, state = "normal", text = self._texts[i][j])
                self._setStatus(row = i, column = j, status = self._defaults[i][j])
                if self._mode == "single":
                    self._buttons[i][j].npset(attribute = "command", value = lambda event = None, i = i, j = j: self._single(row = i, column = j))
                elif self._mode == "multiple":
                    self._buttons[i][j].npset(attribute = "command", value = lambda event = None, i = i, j = j: self._multiple(row = i, column = j))
                self._buttons[i][j].place()
    
    def _setStatus(self, row: int, column: int, status: Literal["default", "active", "disabled"]):
        if status == self._status[row][column]:
            return
        if status == "disabled":
            # self._buttons[row][column].configure(background = self._buttons[row][column].npget(attribute = "disabledbackground"))
            # self._buttons[row][column].configure(state = "disabled")
            self._buttons[row][column].npset(attribute = "state", value = "disabled")
        elif status == "default":
            self._buttons[row][column].configure(activebackground = self._buttons[row][column].npget(attribute = "background"))
            self._buttons[row][column].configure(background = self._buttons[row][column].npget(attribute = "background"))
        elif status == "active":
            self._buttons[row][column].configure(activebackground = self._buttons[row][column].npget(attribute = "activebackground"))
            self._buttons[row][column].configure(background = self._buttons[row][column].npget(attribute = "activebackground"))
        self._status[row][column] = status
    
    def _single(self, row: int, column: int):
        for i in range(self._rows):
            for j in range(self._columns):
                if self._status[i][j] == "disabled":
                    continue
                if i == row and j == column:
                    self._setStatus(row = i, column = j, status = "active")
                else:
                    self._setStatus(row = i, column = j, status = "default")
    
    def _multiple(self, row: int, column: int):
        if self._status[row][column] == "active":
            self._setStatus(row = row, column = column, status = "default")
        elif self._status[row][column] == "default":
            self._setStatus(row = row, column = column, status = "active")
    
    def npset(self, attribute: str, value: Any = None):
        if attribute == "status":
            self._setStatus(row = value[0], column = value[1], status = value[2])
        return super().npset(attribute = attribute, value = value)
    
    def npget(self, attribute: str):
        if attribute == "default" or attribute == "active" or attribute == "disabled":
            result = [[bool for _ in range(self._columns)] for _ in range(self._rows)]
            for i in range(self._rows):
                for j in range(self._columns):
                    if self._status[i][j] == attribute:
                        result[i][j] = True
                    else:
                        result[i][j] = False
            return result
        else:
            return super().npget(attribute = attribute)