from tkinter import Tk
from typing import Literal
from ..Constants.NPScreen import Screen
import hmac
import hashlib
import base64

class NPTk(Tk):
    
    def __init__(self):
        
        super().__init__(screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None)
        
        super().geometry(str(Screen["width"]) + "x" + str(Screen["height"]) + "+" + str(Screen["x"]) + "+" + str(Screen["y"]))
        
        super().overrideredirect(boolean = True)
        
        self._mode: Literal["user", "admin"] = "user"
        self._flows = None
        
        self._state: Literal["normal", "error"] = "normal"
    
        self._error = ""
    
    def mainloop(self):
        super().mainloop()
    
    def destroy(self):
        super().destroy()
    
    def resetFlows(self):
        try:
            self._flows.destroy()
        except:
            pass
        from ..Flows.NPFlows import NPFlows
        self._flows = NPFlows(master = self)
        self._flows.place()
    
    def _nphash(self, password):
        dig = hmac.new(b'NightPanther', msg = password.encode(), digestmod = hashlib.sha256).digest()
        return base64.b64encode(dig).decode()

    def signIn(self, password: str = None):
        if self._mode == "admin":
            return
        if self._nphash(password = password) == 'p2R1aJDLVZ7T/YkgGjVFTqg6M0uciXsGkzmRO8gKpuk=':
            self._mode = "admin"
    
    def signOut(self):
        if self._mode == "user":
            return
        self._mode = "user"
        
    def npget(self, attribute: str):
        if attribute == "mode":
            return self._mode
        if attribute == "state":
            return self._state

    def markErrorFixed(self):
        self._state = "normal"

    def markErrorOccured(self, error):
        self._state = "error"
        self._error = error
