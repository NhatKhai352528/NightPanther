from tkinter import Tk
from typing import Literal
from ..Constants.NPScreen import Screen

class NPTk(Tk):
    
    def __init__(self):
        
        super().__init__(screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None)
        
        super().geometry(str(Screen["width"]) + "x" + str(Screen["height"]) + "+" + str(Screen["x"]) + "+" + str(Screen["y"]))
        
        super().overrideredirect(boolean = True)
        
        self._mode: Literal["user", "admin"] = "user"
    
    def mainloop(self):
        super().mainloop()
    
    def destroy(self):
        super().destroy()
    
    def signIn(self, password: str = None):
        if self._mode == "admin":
            return
        if password == "1611":
            self._mode = "admin"
    
    def signOut(self):
        if self._mode == "user":
            return
        self._mode = "user"
        
    def npget(self, attribute: str):
        if attribute == "mode":
            return self._mode
