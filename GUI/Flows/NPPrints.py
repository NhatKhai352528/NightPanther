from tkinter import Tk
from threading import Thread
from typing import Any
from ..Pages.Prints.NPFormat import NPFormat
from ..Pages.Prints.NPOrder import NPOrder
from ..Pages.Prints.NPPayment import NPPayment
from ..Pages.Prints.NPPrinting import NPPrinting
from ..Pages.Prints.NPSuccess import NPSuccess
from ..Pages.Prints.NPUpload import NPUpload
from ..Constants.NPPrice import Price

class NPPrints:
    
    def __init__(self, master: Tk, destroyCommand: Any):
        
        self._master = master
        self._destroyCommand = destroyCommand
        
        # Pages
        self._upload = None
        self._format = None
        self._order = None
        self._payment = None
        self._printing = None
        self._success = None
        
        # Server variables
        self._serverLink = "Test"
        self._serverKey = "Test"
        
        # File variables
        self._fileName = "Test"
        self._filePaper = None
        self._fileSides = None
        self._filePages = 1000
        self._filePrice = 1000
        
        # User variables
        self._userCopies = None
        self._userPrice = None
        self._userQRFile = None
        
        # Printer variables
        self._printerPage = 0
        self._printerCopy = 0
        
    def place(self):
        getServerVariables = Thread(target = None)
        getServerVariables.start()
        self._upload = NPUpload(master = self._master, commands = [None, lambda event = None: self._uploadToFormat()], serverLink = self._serverLink, serverKey = self._serverKey, fileName = self._fileName)
        self._upload.place()
    
    def destroy(self):
        attributes = ["_upload", "_format", "_order", "_payment", "_printing", "_success"]
        for attribute in attributes:
            try:
                getattr(self, attribute).destroy()
            except:
                pass
        self.__dict__.clear()
    
    def _uploadToFormat(self):
        availablePaper = [list(value.values()) for value in Price.values()]
        availableSides = [[availablePaper[j][i] for j in range(len(availablePaper))] for i in range(len(availablePaper[0]))]
        availablePaper = [False if row == [None, None] else True for row in availablePaper]
        availableSides = [False if row == [None, None, None] else True for row in availableSides]
        self._format = NPFormat(master = self._master, commands = [None, lambda event = None: self._formatToOrder()], fileName = self._fileName, availablePaper = availablePaper, availableSides = availableSides)
        self._format.place()
        self._upload.place_forget()
    
    def _formatToOrder(self):
        self._filePaper = self._format.npget(attribute = "filePaper")
        self._fileSides = self._format.npget(attribute = "fileSides")
        self._filePrice = Price[self._filePaper][self._fileSides]
        if self._order == None:
            self._order = NPOrder(master = self._master, commands = [lambda event = None: self._orderToFormat(), lambda event = None: self._orderToPayment()], fileName = self._fileName, filePrice = self._filePrice)
        else:
            self._order.npset(attribute = "filePrice", value = self._filePrice)
        self._order.place()
        self._format.place_forget()
    
    def _orderToFormat(self):
        self._format.place()
        self._order.place_forget()
    
    def _orderToPayment(self):
        self._userCopies = self._order.npget(attribute = "userCopies")
        self._userPrice = self._order.npget(attribute = "userPrice")
        getUserVariables = Thread(target = None)
        getUserVariables.start()
        self._payment = NPPayment(master = self._master, commands = [None, lambda event = None: self._paymentToPrinting()], fileName = self._fileName, userCopies = self._userCopies, userPrice = self._userPrice, userQRFile = self._userQRFile)
        self._payment.place()
        self._order.place_forget()
    
    def _paymentToPrinting(self):
        self._printing = NPPrinting(master = self._master, commands = [None, lambda event = None: self._printingToSuccess()], fileName = self._fileName, filePages = self._filePages, userCopies = self._userCopies)
        self._printing.place()
        self._payment.place_forget()
    
    def _printingToSuccess(self):
        self._success = NPSuccess(master = self._master, commands = [None, self._destroyCommand])
        self._success.place()
        self._printing.place_forget()
        