from tkinter import Tk
from typing import Any, Literal
from ..NPFrames import NPFrames
from ...Constants.NPWorkspace import Interact
from ...Customs.NPTheme import NPTheme
from ...Objects.NPButtonArray import NPButtonArray
from ...Objects.NPButtonSet import NPButtonSet
from ...Objects.NPKeyBoard import NPKeyBoard
from ...Objects.NPProgressBar import NPProgressBar
from ...Objects.NPSpinBox import NPSpinBox
from ...Widgets.NPImageLabel import NPImageLabel
from ...Widgets.NPTextButton import NPTextButton
from ...Widgets.NPTextLabel import NPTextLabel

class NPInteract(NPFrames):
    
    def __init__(self, master: Tk):

        self._currentTheme = NPTheme.getTheme()
        
        super().__init__(master = master, x = Interact["x"], y = Interact["y"], width = Interact["width"], height = Interact["height"], distance = Interact["distance"], anchor = "nw", background = self._currentTheme["background"]["interact"])
        
        self._currentY = self._distance
    
    def _recheck(self):
        
        # Get current index
        currentIndex = len(self._items) - 1
        
        # This frame does not allow items to exceed its boundaries
        try:
            if self._currentY + self._items[currentIndex].npget(attribute = "height") >= self._height:
                self._items[currentIndex].destroy()
                return None
            else:
                self._items[currentIndex].place()
                self._currentY = self._currentY + self._items[currentIndex].npget(attribute = "height")
                return currentIndex
        # Can not access the currentIndex-th object of the list self._items
        except:
            return None
    
    #
    # NPImageLabel
    
    def initImage(self, imageFile: str, imageWidth: int, imageHeight: int):
        
        self._items.append(NPImageLabel(master = self._frame, x = 0.5 * self._width, y = self._currentY, anchor = "n", background = self.npget(attribute = "background"), imageFile = imageFile, imageWidth = imageWidth, imageHeight = imageHeight))
        
        return self._recheck()
    
    def updateImage(self, index: int, imageFile: str):
        
        if index >= len(self._items):
            return
        if not isinstance(self._items[index], NPImageLabel):
            return
        self._items[index].npset(attribute = "imageFile", value = imageFile)
    
    #
    # NPTextButton
    
    def initButton(self, command: Any, text: str):
        
        currentFont = self._currentTheme["font"]["strong"]
        
        self._items.append(NPTextButton(master = self._frame, mode = "action", x = 0.5 * self._width, y = self._currentY, width = 400, height = 50, anchor = "n", command = command, font = currentFont, repeat = False, state = "normal", text = text))
        
        return self._recheck()
    
    #
    # NPTextLabel
    
    def initText(self, mode: Literal["section", "heading", "content", "small", "footnote"], text: str, justify: Literal["left", "center", "right"]):
        
        # Get current font and foreground
        if mode == "section":
            currentFont = self._currentTheme["font"]["section"]
            currentForeground = self._currentTheme["foreground"]["default"]
        elif mode == "heading":
            currentFont = self._currentTheme["font"]["heading"]
            currentForeground = self._currentTheme["foreground"]["default"]
        elif mode == "content":
            currentFont = self._currentTheme["font"]["normal"]
            currentForeground = self._currentTheme["foreground"]["default"]
        elif mode == "small":
            currentFont = self._currentTheme["font"]["small"]
            currentForeground = self._currentTheme["foreground"]["default"]
        elif mode == "footnote":
            currentFont = self._currentTheme["font"]["tiny"]
            currentForeground = self._currentTheme["foreground"]["default"]
        
        # Define a new text label, place it onto the frame, and update position for the next item
        self._items.append(NPTextLabel(master = self._frame, x = self._distance, y = self._currentY, width = self._width - 2 * self._distance, anchor = "nw", background = self.npget(attribute = "background"), font = currentFont, foreground = currentForeground, justify = justify, text = text, textAnchor = "nw" if justify == "left" else "n" if justify == "center" else "ne", underline = -1, wraplength = self._width - 2 * self._distance))
        
        return self._recheck()
    
    def updateText(self, index: int, text: str):
        
        if index >= len(self._items):
            return
        if not isinstance(self._items[index], NPTextLabel):
            return
        self._items[index].npset(attribute = "text", value = text)
    
    #
    # NPButtonArray
    
    def initButtonArray(self, mode: Literal["single", "multiple"], rows: int, columns: int, defaults: list[list[Literal["default", "active", "disabled"]]] = None, texts: list[list[str]] = None):
        
        currentFont = self._currentTheme["font"]["strong"]
        
        self._items.append(NPButtonArray(master = self._frame, mode = mode, x = 0.5 * self._width, y = self._currentY, distance = self._distance, anchor = "n", background = self.npget(attribute = "background"), rows = rows, columns = columns, widthSize = 100, heightSize = 50, font = currentFont, defaults = defaults, texts = texts))
        
        return self._recheck()
    
    #
    # NPButtonSet
    
    def initButtonSet(self, mode: Literal["single", "multiple"], rows: int, columns: int, defaults: list[list[Literal["default", "active", "disabled"]]] = None, imageFiles: list[list[str]] = None):
        
        self._items.append(NPButtonSet(master = self._frame, mode = mode, x = 0.5 * self._width, y = self._currentY, distance = 2 * self._distance, anchor = "n", background = self.npget(attribute = "background"), rows = rows, columns = columns, widthSize = 200, heightSize = 200, defaults = defaults, imageFiles = imageFiles))
        
        return self._recheck()
    
    #
    # NPKeyBoard
    
    def initKeyBoard(self, default: str = "", maximum: int = 10, show: str = "", inputTexts: list[str] = [None, None], actionTexts: list[str] = None, actionCommands: list[Any] = None):
        
        # Set KeyBoard's font
        entryFont = self._currentTheme["font"]["section"]
        inputFont = self._currentTheme["font"]["heading"]
        actionFont = self._currentTheme["font"]["small"]
        
        self._items.append(NPKeyBoard(master = self._frame, x = 0.5 * self._width, y = self._currentY, distance = self._distance, anchor = "n", background = self.npget(attribute = "background"), size = 50, default = default, maximum = maximum, show = show, entryFont = entryFont, inputFont = inputFont, actionFont = actionFont, inputTexts = inputTexts, actionTexts = actionTexts, actionCommands = actionCommands))
        
        return self._recheck()
    
    #
    # NPProgressBar
    
    def initProgressBar(self, default: float = 0, maximum: float = 0):
        
        self._items.append(NPProgressBar(master = self._frame, x = 0.5 * self._width, y = self._currentY, distance = self._distance, anchor = "n", background = self.npget(attribute = "background"), size = 40, default = default, maximum = maximum))
        
        return self._recheck()
    
    #
    # NPSpinBox
    
    def initSpinBox(self, default: float = 0, minimum: float = 0, maximum: float = 0, step: float = 0, wrap: bool = False, actionCommand: Any = None):
        
        # Set SpinBox's font
        entryFont = self._currentTheme["font"]["section"]
        inputFont = self._currentTheme["font"]["heading"]
        actionFont = self._currentTheme["font"]["small"]
        
        self._items.append(NPSpinBox(master = self._frame, x = 0.5 * self._width, y = self._currentY, distance = self._distance, anchor = "n", background = self.npget(attribute = "background"), size = 50, default = default, minimum = minimum, maximum = maximum, step = step, wrap = wrap, entryFont = entryFont, inputFont = inputFont, actionFont = actionFont, actionCommand = actionCommand))
        
        return self._recheck()
    
    def npget(self, attribute: str, index: Any = None):
        if index == None:
            return super().npget(attribute = attribute)
        if attribute == "buttonArray":
            if index >= len(self._items):
                return
            if not isinstance(self._items[index], NPButtonArray):
                return
            return self._items[index]
        elif attribute == "buttonSet":
            if index >= len(self._items):
                return
            if not isinstance(self._items[index], NPButtonSet):
                return
            return self._items[index]
        elif attribute == "keyBoard":
            if index >= len(self._items):
                return
            if not isinstance(self._items[index], NPKeyBoard):
                return
            return self._items[index]
        elif attribute == "progressBar":
            if index >= len(self._items):
                return
            if not isinstance(self._items[index], NPProgressBar):
                return
            return self._items[index]
        elif attribute == "spinBox":
            if index >= len(self._items):
                return
            if not isinstance(self._items[index], NPSpinBox):
                return
            return self._items[index]