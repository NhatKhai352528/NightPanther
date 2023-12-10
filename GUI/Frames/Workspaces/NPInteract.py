from tkinter import Frame
from typing import Any, Literal
from ..NPFrames import NPFrames
from ...Constants.NPWorkspace import Interact
from ...Customs.NPTheme import NPTheme
from ...Objects.NPButtonArray import NPButtonArray
from ...Objects.NPKeyBoard import NPKeyBoard
from ...Objects.NPProgressBar import NPProgressBar
from ...Objects.NPSpinBox import NPSpinBox
from ...Widgets.NPImageLabel import NPImageLabel
from ...Widgets.NPTextLabel import NPTextLabel

currentTheme = NPTheme.getTheme()

class NPInteract(NPFrames):
    
    def __init__(self, master: Frame):
        
        super().__init__(master = master, x = Interact["x"], y = Interact["y"], width = Interact["width"], height = Interact["height"], distance = Interact["distance"], anchor = "nw", background = currentTheme["background"]["interact"])
        
        self._currentY = self._distance
    
    def _recheck(self):
        
        # Get current index
        currentIndex = len(self._items) - 1
        
        # This frame does not allow items to exceed its boundaries
        try:
            if self._currentY + self._items[currentIndex].npget("height") >= self._height:
                self._items[currentIndex].destroy()
                return -1
            else:
                self._items[currentIndex].place()
                self._currentY = self._currentY + self._items[currentIndex].npget("height")
                return currentIndex
        # Can not access the currentIndex-th object of the list self._items
        except:
            return -1
    
    #
    # NPImageLabel
    
    def initImage(self, imageFile: str, imageWidth: int, imageHeight: int):
        
        self._items.append(NPImageLabel(master = self._frame, x = 0.5 * self._width, y = self._currentY, anchor = "n", background = self.npget("background"), imageFile = imageFile, imageWidth = imageWidth, imageHeight = imageHeight))
        
        return self._recheck()
    
    def updateImage(self, index: int, imageFile: str):
        
        if index >= len(self._items):
            return
        if not isinstance(self._items[index], NPImageLabel):
            return
        self._items[index].setImage(imageFile)
    
    #
    # NPTextLabel
    
    def initText(self, mode: Literal["section", "heading", "content"], text: str, justify: Literal["left", "center", "right"]):
        
        # Get current font and foreground
        if mode == "section":
            currentFont = currentTheme["font"]["section"]
            currentForeground = currentTheme["foreground"]["default"]
        elif mode == "heading":
            currentFont = currentTheme["font"]["heading"]
            currentForeground = currentTheme["foreground"]["default"]
        elif mode == "content":
            currentFont = currentTheme["font"]["normal"]
            currentForeground = currentTheme["foreground"]["default"]
        
        # Define a new text label, place it onto the frame, and update position for the next item
        self._items.append(NPTextLabel(master = self._frame, x = self._distance, y = self._currentY, width = self._width - 2 * self._distance, anchor = "nw", background = self.npget("background"), font = currentFont, foreground = currentForeground, justify = justify, text = text, textAnchor = "nw" if justify == "left" else "n" if justify == "center" else "ne", underline = -1, wraplength = self._width - 2 * self._distance))
        
        return self._recheck()
    
    def updateText(self, index: int, text: str):
        
        if index >= len(self._items):
            return
        if not isinstance(self._items[index], NPTextLabel):
            return
        self._items[index].setText(text)
    
    #
    # NPButtonArray
    
    def initButtonArray(self, mode: Literal["single", "multiple", "voting"], rows: int, columns: int, defaults: list[list[Literal["default", "active", "disabled"]]] = None, texts: list[list[str]] = None):
        
        currentFont = currentTheme["font"]["strong"]
        
        self._items.append(NPButtonArray(master = self._frame, mode = mode, x = 0.5 * self._width, y = self._currentY, distance = self._distance, anchor = "n", background = self.npget("background"), rows = rows, columns = columns, widthSize = 100, heightSize = 50, font = currentFont, defaults = defaults, texts = texts))
        
        return self._recheck()
    
    #
    # NPKeyBoard
    
    def initKeyBoard(self, default: str = "", maximum: int = 10, show: str = "", inputTexts: list[str] = [None, None], actionTexts: list[str] = None, actionCommands: list[Any] = None):
        
        # Set KeyBoard's font
        entryFont = currentTheme["font"]["section"]
        inputFont = currentTheme["font"]["heading"]
        actionFont = currentTheme["font"]["small"]
        
        self._items.append(NPKeyBoard(master = self._frame, x = 0.5 * self._width, y = self._currentY, distance = self._distance, anchor = "n", background = self.npget("background"), size = 50, default = default, maximum = maximum, show = show, entryFont = entryFont, inputFont = inputFont, actionFont = actionFont, inputTexts = inputTexts, actionTexts = actionTexts, actionCommands = actionCommands))
        
        return self._recheck()
    
    #
    # NPProgressBar
    
    def initProgressBar(self, default: float = 0, maximum: float = 0):
        
        self._items.append(NPProgressBar(master = self._frame, x = 0.5 * self._width, y = self._currentY, distance = self._distance, anchor = "n", background = self.npget("background"), size = 40, default = default, maximum = maximum))
        
        return self._recheck()
    
    #
    # NPSpinBox
    
    def initSpinBox(self, default: float = 0, minimum: float = 0, maximum: float = 0, step: float = 0, wrap: bool = False, actionText: str = None, actionCommand: Any = None):
        
        # Set SpinBox's font
        entryFont = currentTheme["font"]["section"]
        inputFont = currentTheme["font"]["heading"]
        actionFont = currentTheme["font"]["small"]
        
        self._items.append(NPSpinBox(master = self._frame, x = 0.5 * self._width, y = self._currentY, distance = self._distance, anchor = "n", background = self.npget("background"), size = 50, default = default, minimum = minimum, maximum = maximum, step = step, wrap = wrap, entryFont = entryFont, inputFont = inputFont, actionFont = actionFont, actionText = actionText, actionCommand = actionCommand))
        
        return self._recheck()