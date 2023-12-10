from tkinter import Tk
from threading import Thread
from .NPFormat import NPFormat
from .NPUpload import NPUpload
from .NPWelcome import NPWelcome

class NPPrints:
    
    def __init__(self, master: Tk):
        
        self._master = master
        
        # Pages
        self._upload = None
        self._format = None
        
        # Variables
        self._serverLink = None
        self._serverKey = None
        
        self._fileName = None
        
        # Initialize the first page of this flow
        Thread(target = None).start()
        self._upload = NPUpload(master = self._master, commands = [None, lambda event = None: self._uploadToFormat()], serverLink = self._serverLink, serverKey = self._serverKey, fileName = self._fileName)
        self._upload.place()
    
    def _uploadToFormat(self):
        self._format = NPFormat(master = self._master, commands = [None, None], fileName = self._fileName)
        self._format.place()
        self._upload.place_forget()