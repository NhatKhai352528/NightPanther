from tkinter import Tk
from typing import Any
from ..Constants.NPScreen import Screen
from ..Customs.NPTheme import NPTheme
from ..Widgets.NPFrame import NPFrame
from ..Widgets.NPMessage import NPMessage
from ..Widgets.NPTextButton import NPTextButton
from ..Widgets.NPToplevel import NPToplevel

class NPConfirmBox:
    
    def __init__(self, master: Tk, messageText: str, buttonTexts: list[str], buttonCommands: list[Any]):

        self._currentTheme = NPTheme.getTheme()
        
        self._master = master
        
        # Location variables
        self._width = 0.5 * Screen["width"]
        self._height = 0.5 * Screen["height"]
        self._distance = Screen["distance"]
        self._x = (Screen["width"] - self._width) / 2
        self._y = (Screen["height"] - self._height) / 2
        
        self._overlay = NPToplevel(master = self._master, x = Screen["x"], y = Screen["y"], width = Screen["width"], height = Screen["height"], background = self._currentTheme["background"]["default"])
        self._overlay.wait_visibility()
        self._overlay.wm_attributes("-alpha", 0.5)
        
        self._toplevel = NPToplevel(master = self._master, x = self._x, y = self._y, width = self._width, height = self._height, background = self._currentTheme["background"]["confirm"])
        self._toplevel.wait_visibility()
        self._toplevel.wm_attributes("-topmost", True)
        self._toplevel.grab_set()
        
        self._frame = NPFrame(master = self._toplevel, x = 0, y = 0, width = self._width, height = self._height, anchor = "nw", background = self._currentTheme["background"]["confirm"])
        self._frame.place()
        
        self._messageText = messageText
        self._buttonTexts = [str, str]
        for i in range(2):
            try:
                self._buttonTexts[i] = buttonTexts[i]
            except:
                self._buttonTexts[i] = None
        commands = [Any, Any]
        for i in range(2):
            try:
                commands[i] = buttonCommands[i]
            except:
                commands[i] = None
        self._buttonCommands = [Any, Any]
        for i in range(2):
            if commands[i] != None:
                self._buttonCommands[i] = lambda event = None, i = i: (self.destroy(), commands[i]())
            else:
                self._buttonCommands[i] = lambda event = None: self.destroy()
        
        # Size variables
        self._messageWidth = int(self._width - 2 * self._distance)
        self._messageHeight = int(0.75 * self._height - 2 * self._distance)
        self._buttonWidth = int((self._width - 3 * self._distance) / 2)
        self._buttonHeight = int(self._height - self._messageHeight - 3 * self._distance)
        
        self._message = NPMessage(master = self._frame, x = self._distance, y = self._distance, width = self._messageWidth, height = self._messageHeight, anchor = "nw", background = self._currentTheme["background"]["default"], font = self._currentTheme["font"]["heading"], foreground = self._currentTheme["foreground"]["highlight"], text = self._messageText)
        self._message.place()
        
        self._buttons = [Any, Any]
        for i in range(2):
            self._buttons[i] = NPTextButton(master = self._frame, mode = "action", x = i * self._buttonWidth + (i + 1) * self._distance, y = self._messageHeight + 2 * self._distance, width = self._buttonWidth, height = self._buttonHeight, anchor = "nw", command = self._buttonCommands[i], font = self._currentTheme["font"]["strong"], repeat = False, state = "normal" if self._buttonTexts[i] != None else "disabled", text = self._buttonTexts[i])
            self._buttons[i].place()
        
    def destroy(self):
        self._overlay.destroy()
        self._toplevel.destroy()
