from tkinter import Tk
from threading import Thread, Timer, Event
from typing import Any
from ..Pages.Prints.NPFormat import NPFormat
from ..Pages.Prints.NPOrder import NPOrder
from ..Pages.Prints.NPPayment import NPPayment
from ..Pages.Prints.NPPrinting import NPPrinting
from ..Pages.Prints.NPSuccess import NPSuccess
from ..Pages.Prints.NPUpload import NPUpload
from ..Constants.NPPrice import Price
import subprocess
import qrcode
import random
import globals
from PyPDF2 import PdfReader, PdfWriter
from ..Customs.NPLanguage import NPLanguage
from ..Objects.NPConfirmBox import NPConfirmBox

currentLanguage = NPLanguage.getLanguage()

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
        self._upload = NPUpload(master = self._master, commands = [None, lambda event = None: self._uploadToFormat()], serverLink = self._serverLink, serverKey = self._serverKey, fileName = self._fileName)
        self._upload.place()
        getServerVariables = Thread(target = self._getServerVariables)
        getServerVariables.start()
    
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
        reader = PdfReader("../CO3091_BE/user_file.pdf")
        self._filePrice = Price[self._filePaper][self._fileSides] * len(reader.pages)
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
        self._printing = NPPrinting(master = self._master, commands = [None, None], fileName = self._fileName, filePages = self._filePages, userCopies = self._userCopies)
        self._printing.initControlButton(position = "left", command = lambda event = None: self._orderCancelAlert(), state = "normal", text = currentLanguage["printing"]["control"]["cancel"])
        self._printing.initControlButton(position = 'right', command = lambda event = None: self._printToPause(), state = 'normal', text = currentLanguage["printing"]["control"]["pause"])
        self.pauseEvent = Event() 
        self._printing.place()
        self._payment.place_forget()
        printUserFile = Thread(target = self._printUserFile)
        printUserFile.start()
    
    def _printingToSuccess(self):
        self._success = NPSuccess(master = self._master, commands = [None, self._destroyCommand])
        self._success.place()
        self._printing.place_forget()

    def _orderCancelAlert(self):
        self._printToPause()
        NPConfirmBox(master = self._master, messageText = "NguyenThiTam", buttonTexts = ["cancel", "OK"], buttonCommands = [None, lambda event = None: self._printingToSuccess()])

    def _printToPause(self):
        self.pauseEvent.set()
        self._printing.initControlButton(position = 'right', command = lambda event = None: self._pauseToPrint(), state = 'normal', text = currentLanguage["printing"]["control"]["continue"])
    
    def _pauseToPrint(self):
        self.pauseEvent.clear()
        self._printing.initControlButton(position = 'right', command = lambda event = None: self._printToPause(), state = 'normal', text = currentLanguage["printing"]["control"]["pause"])
    
    def _getServerVariables(self):
        # self._serverLink = subprocess.check_output(['hostname','-I']).decode().strip().split()[0] + ':3000'
        self._upload.npset(attribute = "serverLink", value = self._serverLink)
        uploadQR = qrcode.make("http://" + self._serverLink)
        type(uploadQR)
        uploadQR.save("GUI/Images/UploadQR.png")
        self._upload.npset(attribute = "serverQRFile", value = "GUI/Images/UploadQR.png")

        random.seed()
        self.printingCode = random.randint(100000, 999999)
        self._serverKey = str(self.printingCode)
        self._upload.npset(attribute = "serverKey", value = self._serverKey)
        self._fileName = "Waiting for user to upload file ..."
        self._upload.npset(attribute = "fileName", value = self._fileName)
        
        def _listenWebServer():
            globals.webServerSocket.send(str(self.printingCode).encode())
            self._fileName = globals.webServerSocket.recv(1024).decode()
            self._upload.npset(attribute = "fileName", value = self._fileName)
        listenWebServer = Thread(target = _listenWebServer)
        listenWebServer.start()

    def _printUserFile(self):        
        reader = PdfReader("../CO3091_BE/user_file.pdf")
        
        def isPageLandscape(pageIndex):
            page = reader.pages[pageIndex]
            rotation = page.get('/Rotate')
            mediabox = page.mediabox

            # Landscape attribute
            if mediabox.right > mediabox.top:
                if rotation in [0, 180, None]:
                    return True
                else:
                    return False
            else:
                if rotation in [0, 180, None]:
                    return False
                else:
                    return True
        
        def getFileSize():
            fileSize = self._format.npget(attribute = "filePaper")
            if (fileSize == "a3"):
                return "A3"
            if (fileSize == "a4"):
                return "A4"
            if (fileSize == "a5"):
                return "A5"
        
        # For test
        def handlePrintError(strError):
            print(strError)

        def getSideOption():
            sideOption = self._format.npget(attribute = "fileSides")
            if (sideOption == "1s"):
                return "one-sided"
            if (sideOption == "2s"):
                return "two-sided-short-edge" # For test
        
        self._filePages = len(reader.pages)
        self._printing.npset(attribute = "userCopies", value = self._userCopies)
        self._printing.npset(attribute = "filePages", value = self._filePages)
        # Printing
        for _ in range(0, self._userCopies):
            for page in range(0, self._filePages):
                writer = PdfWriter()
                writer.add_page(reader.pages[page])
                with open("../CO3091_BE/current_page.pdf", "wb") as fp:
                    writer.write(fp)
                
                printerFile = open("printer.txt")
                printerName = printerFile.read().strip()
                printCommand = ["lp", "-d", printerName, "-o","media=" + getFileSize(), "-n", "1", "-o", "sides=" + getSideOption(), "-o", "fit-to-page"]
                if isPageLandscape(page):
                    printCommand.extend(["-o", "landscape]"])
                printCommand.append("../CO3091_BE/current_page.pdf")
                subprocess.run(printCommand)
                
                # Time out for error
                def printingTimeOut():
                    printer_status = subprocess.check_output(["lpstat", "-p", printerName]).decode().lower();
                    if (printer_status.find("idle") != -1):
                        handlePrinterError(strError = "nono")
                    elif (printer_status.find("rendering completed") != -1):
                        handlePrintError(strError = "The printer is not working properly")
                    elif (printer_status.find("sending data to printer") != -1):
                        handlePrintError(strError = "There's an error in our system")
                    else:
                        handlePrintError(strError = "Unknown error")
                printTimeOut = Timer(2.0, printingTimeOut)
                printTimeOut.start()

                while True:
                    printer_status = subprocess.check_output(["lpstat", "-p", printerName]).decode()
                    if (printer_status.find("idle") != -1):
                        break
                # Print successfully, cancel the error time out
                printTimeOut.cancel()

                # Update GUI
                if self._printerCopy < self._userCopies:
                    self._printerPage = self._printerPage + 1
                if self._printerPage > self._filePages:
                    self._printerPage = 1
                if self._printerPage == self._filePages:
                    self._printerCopy = self._printerCopy + 1
                if self._printerCopy >= self._userCopies:
                    self._printingToSuccess()
                            
                self._printing.npset(attribute = "printerPage", value = self._printerPage)
                self._printing.npset(attribute = "printerCopy", value = self._printerCopy)
                
                while (self._printerCopy < self._userCopies and self.pauseEvent.is_set()):
                    pass
        
