from tkinter import Tk
from threading import Thread, Event
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

import requests
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from ..Objects.NPConfirmBox import NPConfirmBox
from selenium.common.exceptions import NoSuchElementException
from ..Customs.NPLanguage import NPLanguage

class NPPrints:
    
    def __init__(self, master: Tk, destroyCommand: Any):

        self._currentLanguage = NPLanguage.getLanguage()
        
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
        # Reset web server to waiting for new order
        resetMessage = "reset"
        globals.webServerSocket.send(resetMessage.encode())
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
        reader = PdfReader("./CO3091_BE/user_file.pdf")
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
        self._payment = NPPayment(master = self._master, commands = [None, lambda event = None: self._paymentCancelAlert()], fileName = self._fileName, userCopies = self._userCopies, userPrice = self._userPrice, userQRFile = self._userQRFile)
        self._payment.place()
        self._order.place_forget()
        self.paymentCancelEvent = Event()
        generateQR = Thread(target = self._generateQR)
        generateQR.start()
        paymentCheck = Thread(target = self._paymentCheck)
        paymentCheck.start()
    
    def _paymentToPrinting(self):
        self._printing = NPPrinting(master = self._master, commands = [None, None], fileName = self._fileName, filePages = self._filePages, userCopies = self._userCopies)
        self._printing.initControlButton(position = "left", command = lambda event = None: self._orderCancelAlert(), state = "normal", text = self._currentLanguage["printing"]["control"]["cancel"])
        self._printing.initControlButton(position = 'right', command = lambda event = None: self._printToPause(), state = 'normal', text = self._currentLanguage["printing"]["control"]["pause"])
        self.pauseEvent = Event()
        self.stopEvent = Event()
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
        NPConfirmBox(master = self._master, messageText = "NguyenThiTam", buttonTexts = ["cancel", "OK"], buttonCommands = [None, lambda event = None: self._printCancelOrder()])

    def _printCancelOrder(self):
        self.stopEvent.set()
        self._printingToSuccess()

    def _printToPause(self):
        self.pauseEvent.set()
        self._printing.initControlButton(position = 'right', command = lambda event = None: self._pauseToPrint(), state = 'normal', text = self._currentLanguage["printing"]["control"]["continue"])
    
    def _adminPauseToPrint(self):
        if self._master.npget(attribute = "mode") == "admin":
            self._pauseToPrint()

    def _pauseToPrint(self):
        self.pauseEvent.clear()
        self._printing.initControlButton(position = 'right', command = lambda event = None: self._printToPause(), state = 'normal', text = self._currentLanguage["printing"]["control"]["pause"])
    
    def _paymentToSuccess(self):
        self._success = NPSuccess(master = self._master, commands = [None, self._destroyCommand])
        self._success.place()
        self._payment.place_forget()

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
    
    def _paymentCancelAlert(self):
        NPConfirmBox(master = self._master, messageText = "Bạn có chắc muốn hủy đơn", buttonTexts = ["Có", "Không"], buttonCommands = [lambda event = None: self._paymentCancel(), None])

    def _paymentCancel(self):
        self.paymentCancelEvent.set()
        subprocess.run(["pkill", "-9", "chromium-browse"])
        self._paymentToSuccess()

    def _generateQR(self):
        cost = str(self._userPrice)
        head_url="https://img.vietqr.io/image/ocb-0004100037889007-HgRYJqu.png?amount="
        tail_url="&addInfo=SSPS%20" + str(self._serverKey) + "&accountName=Pham%20Van%20Nhat%20Vu"
        url=head_url+cost+tail_url
        try:
            urllib.request.urlretrieve(url, "GUI/Images/PaymentQR.png")
            self._payment.npset(attribute = "userQRFile", value = "GUI/Images/PaymentQR.png")
        except urllib.error.URLError:
            self._master.after(100, NPConfirmBox, self._master, "Mat ket noi mang, vui long lien he", [None, "OK"], [None, lambda event = None: self._paymentCancel()])
    
    def _paymentCheck(self): 
        try:
            googleUserInfo = "/home/pi/Desktop/NPPayCheck"
            option = webdriver.ChromeOptions()
            option.add_argument("user-data-dir=" + googleUserInfo)
            driver = Service('/usr/lib/chromium-browser/chromedriver')
            browser = webdriver.Chrome(service = driver, options = option)
            browser.get("https://mightytext.net")
            sleep(20)
        
            # Login to Mighty Text Web
            login = browser.find_element(By.ID,'login')
            login.click()
            sleep(20)
        
            # Check for web notification and close
            while True:
                try:
                    noti_list = browser.find_element(By.CLASS_NAME, 'intercom-post-close')
                except NoSuchElementException:
                    break
                for close_button in noti_list:
                    close_button.click()
            sleep(10)

            # Click to the message sent by OCB
            click_ocb = browser.find_element(By.ID,'thread-78062')
            click_ocb.click()
            sleep(10)

            # Wait for new message
         
            while True:
                if self.paymentCancelEvent.is_set():
                    return
                messageIndex = 0
                notFoundNewMessage = True
                while True:
                    messageIndex = messageIndex + 1
                    try:
                        messageList = browser.find_elements(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div[2]/div[1]')
                    except NoSuchElementException:
                        break

                    for message in messageList:
                        break
                
                    # Latest message with SSPS format
                    text = message.text
                    if text.find("SSPS") != -1:
                        notFoundNewMessage = False
                        break
                if notFoundNewMessage:
                    continue

                code = text[text.find("SSPS") + 5:text.find("SSPS") + 12].strip()
                if (int(code) == int(self._serverKey)):
                    break
        
            paymentStr = text[text.find("(+)")+4:text.find("VND")]
            payment = int(paymentStr.replace(',',''))
            browser.close()
        
            if (payment == self._userPrice):
                self._paymentToPrinting()
            else:
                self._master.after(100, NPConfirmBox, self._master, "Nop sai rui, lien he de gui lai", [None, "OK"], [None, lambda event = None: self._paymentToSuccess(), None])
        except Exception as e:
            print(str(e))
            try:
                if self.paymentCancelEvent.is_set() == False:
                    self._master.after(100, NPConfirmBox, self._master, "He thong kiem tra thanh toan xay ra loi", [None, "OK"], [None, lambda event = None: self._paymentToSuccess(), None])
            except Exception:
                return
    def _printUserFile(self):        
        reader = PdfReader("./CO3091_BE/user_file.pdf")
        
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
        
        def handlePrintError(strError):
            self.pauseEvent.set()
            self._printing.initControlButton(position = 'right', command = lambda event = None: self._adminPauseToPrint(), state = 'normal', text = self._currentLanguage["printing"]["control"]["continue"])
            NPConfirmBox(master = self._master, messageText = strError, buttonTexts = [None, "OK"], buttonCommands = [None, None])

        def getSideOption():
            sideOption = self._format.npget(attribute = "fileSides")
            if (sideOption == "1s"):
                return "one-sided"
            if (sideOption == "2s"):
                return "two-sided-short-edge" # For test
        
        self._filePages = len(reader.pages)
        self._printing.npset(attribute = "userCopies", value = self._userCopies)
        
        self._filePages = len(reader.pages)
        self._printing.npset(attribute = "userCopies", value = self._userCopies)
        self._printing.npset(attribute = "filePages", value = self._filePages)
        # Printing
        for _ in range(0, self._userCopies):
            for page in range(0, self._filePages):
                if self.stopEvent.is_set():
                    return
                writer = PdfWriter()
                writer.add_page(reader.pages[page])
                with open("./CO3091_BE/current_page.pdf", "wb") as fp:
                    writer.write(fp)
                
                printerFile = open("printer.txt")
                printerName = printerFile.read().strip()
                printCommand = ["lp", "-d", printerName, "-o","media=" + getFileSize(), "-n", "1", "-o", "sides=" + getSideOption(), "-o", "fit-to-page"]
                if isPageLandscape(page):
                    printCommand.extend(["-o", "landscape]"])
                printCommand.append("./CO3091_BE/current_page.pdf")
                
                try:
                    subprocess.run(printCommand, check = True)
                except subprocess.CalledProcessError as e:
                    self._master.after(100, handlePrintError, "There's an error in printing command")
                    return

                # Time out for error
                def printingTimeOut():
                    printer_status = subprocess.check_output(["lpstat", "-p", printerName]).decode().lower();
                    if (printer_status.find("idle") != -1):
                        pass
                    elif (printer_status.find("rendering completed") != -1):
                        handlePrintError(strError = "The printer is not working properly")
                    elif (printer_status.find("sending data to printer") != -1):
                        handlePrintError(strError = "There's an error in our system")
                    else:
                        handlePrintError(strError = "Unknown error")
                timeOutId = self._master.after(1000, printingTimeOut)
                isCommandError = False
                while True:
                    try:
                        printer_status = subprocess.check_output(["lpstat", "-p", printerName]).decode()
                    except subprocess.CalledProcessError as e:
                        self._master.after(100, handlePrintError, "There's an error in printing command")
                        isCommandError = True
                    if (printer_status.find("idle") != -1):
                        break
                if isCommandError:
                    return
                # Print successfully, cancel the error time out
                self._master.after_cancel(timeOutId)

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
                
                while (self._printerCopy < self._userCopies and self.pauseEvent.is_set() and self.stopEvent.is_set() == False):
                    pass
        
