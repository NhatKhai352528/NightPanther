from tkinter import Tk
from time import strftime
from typing import Any
from ..Frames.NPMenu import NPMenu
from ..Frames.NPStatus import NPStatus

class NPBars:
    
    def __init__(self, master: Tk, menuCommands: list[Any] = None):
        
        self._master = master
        
        # Passed commands handler
        self._menuCommands = [Any, Any, Any, Any]
        for i in range(4):
            try:
                self._menuCommands[i] = menuCommands[i]
            except:
                self._menuCommands[i] = None
        
        self._menu = NPMenu(master = self._master)
        self._status = NPStatus(master = self._master)
        
        self._menu.initButton(index = 0, command = self._menuCommands[0], imageFile = None, state = "normal")
        self._menu.initButton(index = 1, command = self._menuCommands[1], imageFile = None, state = "normal")
        self._menu.initButton(index = 2, command = self._menuCommands[2], imageFile = None, state = "normal")
        self._menu.initButton(index = 3, command = self._menuCommands[3], imageFile = None, state = "normal")
        
        self._status.initImage(anchor = "w", imageFile = None)
        self._status.initImage(anchor = "e", imageFile = None)
        self._status.initText(width = 400, anchor = "w", text = "Student Smart Printing System")
        
        self._statusFrame = self._status.npget(attribute = "frame")
        self._clockIndex = self._status.initText(width = 150, anchor = "e", text = "")
        self._updateClock()
    
    def place(self):
        self._menu.place()
        self._status.place()
    
    def place_forget(self):
        self._menu.place_forget()
        self._status.place_forget()
    
    def destroy(self):
        self._menu.destroy()
        self._status.destroy()
    
    def _updateClock(self):
        currentTime = strftime("%H:%M:%S")
        self._status.updateText(index = self._clockIndex, text = currentTime)
        self._statusFrame.after(500, self._updateClock)