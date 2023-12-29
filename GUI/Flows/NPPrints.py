from tkinter import Tk
from threading import Thread, Event
from typing import Any
from ..Pages.Prints.NPFormat import NPFormat
from ..Pages.Prints.NPFlip import NPFlip
from ..Pages.Prints.NPOrder import NPOrder
from ..Pages.Prints.NPPayment import NPPayment
from ..Pages.Prints.NPPrinting import NPPrinting
from ..Pages.Prints.NPSuccess import NPSuccess
from ..Pages.Prints.NPUpload import NPUpload
from ..Constants.NPPaperPrice import PaperPrice
from ..Constants.NPInkPrice import InkPrice
from ..Constants.NPPaper import Paper
from ..Constants.NPSides import Sides
import subprocess
import qrcode
import random
import globals
from paymentAccount import PaymentAccount
from PyPDF2 import PdfReader, PdfWriter
from ..Customs.NPLanguage import NPLanguage
from ..Objects.NPConfirmBox import NPConfirmBox

import requests
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from ..Objects.NPConfirmBox import NPConfirmBox
from selenium.common.exceptions import NoSuchElementException
from ..Customs.NPLanguage import NPLanguage

from datetime import datetime

class NPPrints:
    
    def __init__(self, master: Tk, destroyCommand: Any):

        self._currentLanguage = NPLanguage.getLanguage()
        
        self._master = master
        self._destroyCommand = destroyCommand
        
        # Pages
        self._upload = None
        self._format = None
        self._flip = None
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
        self._fileFlip = None
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
        attributes = ["_upload", "_format", "_flip", "_order", "_payment", "_printing", "_success"]
        for attribute in attributes:
            try:
                getattr(self, attribute).destroy()
            except:
                pass
        self.__dict__.clear()
    
    def _uploadToFormat(self):
        # User not upload file
        if self._fileName == self._waitingText:
            NPConfirmBox(master = self._master, messageText = self._currentLanguage["popup"]["guide"]["uploadBeforeFormat"], buttonTexts = [None, "OK"], buttonCommands = [None, None])
            return
        # Reset web server to waiting for new order
        resetMessage = "reset"
        globals.webServerSocket.send(resetMessage.encode())
        availablePaper = Paper.values()
        availableSides = Sides.values()
        self._format = NPFormat(master = self._master, commands = [None, lambda event = None: self._formatToFlip()], fileName = self._fileName, availablePaper = availablePaper, availableSides = availableSides)
        self._format.place()
        self._upload.place_forget()
    
    def _formatToFlip(self):
        self._filePaper = self._format.npget(attribute = "filePaper")
        self._fileSides = self._format.npget(attribute = "fileSides")
        if self._fileSides == "1s":
            self._formatToOrder()
            return
        if self._flip == None:
            self._flip = NPFlip(master = self._master, commands = [lambda event = None: self._flipToFormat(), lambda event = None: self._flipToOrder()], fileLayout = "landscape" if self._isPageLandscape(0, PdfReader("../CO3091_BE/user_file.pdf")) else "portrait")
            # self._flip = NPFlip(master = self._master, commands = [lambda event = None: self._flipToFormat(), lambda event = None: self._flipToOrder()], fileLayout = "landscape" if self._isPageLandscape(0, PdfReader("./CO3091_BE/user_file.pdf")) else "portrait")
        else:
            self._flip.npset(attribute = "fileLayout", value = "landscape" if self._isPageLandscape(0, PdfReader("../CO3091_BE/user_file.pdf")) else "portrait")
            # self._flip.npset(attribute = "fileLayout", value = "landscape" if self._isPageLandscape(0, PdfReader("./CO3091_BE/user_file.pdf")) else "portrait")
        self._flip.place()
        self._format.place_forget()
    
    def _flipToFormat(self):
        self._format.place()
        self._flip.place_forget()
    
    def _formatToOrder(self):
        reader = PdfReader("../CO3091_BE/user_file.pdf")
        # reader = PdfReader("./CO3091_BE/user_file.pdf")
        self._filePrice = PaperPrice[self._filePaper] * len(reader.pages)
        if self._fileSides == "1s":
            self._filePrice = self._filePrice + InkPrice[self._filePaper] * len(reader.pages)
        else:
            self._filePrice = self._filePrice + 2 * InkPrice[self._filePaper] * len(reader.pages)
        if self._order == None:
            self._order = NPOrder(master = self._master, commands = [lambda event = None: self._orderToFormat(), lambda event = None: self._orderToPayment()], fileName = self._fileName, filePrice = self._filePrice)
        else:
            self._order.npset(attribute = "filePrice", value = self._filePrice)
            self._order.initControlButton(position = "left", command = lambda event = None: self._orderToFormat(), state = "normal", text = self._currentLanguage["order"]["control"]["left"])
        self._order.place()
        self._format.place_forget()

    def _flipToOrder(self):
        self._fileFlip = self._flip.npget(attribute = "fileFlip")
        reader = PdfReader("../CO3091_BE/user_file.pdf")
        # reader = PdfReader("./CO3091_BE/user_file.pdf")
        self._filePrice = PaperPrice[self._filePaper] * len(reader.pages)
        if self._fileSides == "1s":
            self._filePrice = self._filePrice + InkPrice[self._filePaper] * len(reader.pages)
        else:
            self._filePrice = self._filePrice + 2 * InkPrice[self._filePaper] * len(reader.pages)
        if self._order == None:
            self._order = NPOrder(master = self._master, commands = [lambda event = None: self._orderToFlip(), lambda event = None: self._orderToPayment()], fileName = self._fileName, filePrice = self._filePrice)
        else:
            self._order.npset(attribute = "filePrice", value = self._filePrice)
            self._order.initControlButton(position = "left", command = lambda event = None: self._orderToFlip(), state = "normal", text = self._currentLanguage["order"]["control"]["left"])
        self._order.place()
        self._flip.place_forget()
    
    def _orderToFlip(self):
        self._flip.place()
        self._order.place_forget()
   
    def _orderToFormat(self):
        self._format.place()
        self._order.place_forget()

    def _orderToPayment(self):
        self._userCopies = self._order.npget(attribute = "userCopies")
        self._userPrice = self._order.npget(attribute = "userPrice")
        self._payment = NPPayment(master = self._master, commands = [None, lambda event = None: self._paymentCancelAlert()], serverKey = self._serverKey, fileName = self._fileName, userCopies = self._userCopies, userPrice = self._userPrice, userQRFile = self._userQRFile)
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
        NPConfirmBox(master = self._master, messageText = self._currentLanguage["popup"]["confirm"]["reset"], buttonTexts = [self._currentLanguage["popup"]["options"]["remain"], self._currentLanguage["popup"]["options"]["return"]], buttonCommands = [None, lambda event = None: self._printCancelOrder()])

    def _printCancelOrder(self):
        self.stopEvent.set()
        self._printingToSuccess()

    def _printToPause(self):
        self.pauseEvent.set()
        self._printing.initControlButton(position = 'right', command = lambda event = None: self._pauseToPrint(), state = 'normal', text = self._currentLanguage["printing"]["control"]["continue"])
    
    def _adminPauseToPrint(self):
        if self._master.npget(attribute = "mode") == "admin":
            self._pauseToPrint()
        else:
            NPConfirmBox(master = self._master, messageText = self._currentLanguage["popup"]["error"]["systemError"], buttonTexts = [None, "OK"], buttonCommands = [None, None])

    def _pauseToPrint(self):
        self.pauseEvent.clear()
        self._printing.initControlButton(position = 'right', command = lambda event = None: self._printToPause(), state = 'normal', text = self._currentLanguage["printing"]["control"]["pause"])
    
    def _getServerVariables(self):
        self._serverLink = subprocess.check_output(['hostname','-I']).decode().strip().split()[0] + ':3000'
        self._upload.npset(attribute = "serverLink", value = self._serverLink)
        uploadQR = qrcode.make("http://" + self._serverLink)
        type(uploadQR)
        uploadQR.save("GUI/Images/UploadQR.png")
        self._upload.npset(attribute = "serverQRFile", value = "GUI/Images/UploadQR.png")

        random.seed()
        self.printingCode = random.randint(100000, 999999)
        self._serverKey = str(self.printingCode)
        self._upload.npset(attribute = "serverKey", value = self._serverKey)
        self._waitingText = self._currentLanguage["upload"]["data"]["text4"]
        self._fileName = self._waitingText
        self._upload.npset(attribute = "fileName", value = self._fileName)
        
        def _listenWebServer():
            globals.webServerSocket.send(str(self.printingCode).encode())
            self._fileName = globals.webServerSocket.recv(1024).decode()
            self._upload.npset(attribute = "fileName", value = self._fileName)
        listenWebServer = Thread(target = _listenWebServer)
        listenWebServer.start()
    
    def _paymentCancelAlert(self):
        NPConfirmBox(master = self._master, messageText = self._currentLanguage["popup"]["confirm"]["cancelOrder"], buttonTexts = [self._currentLanguage["popup"]["options"]["remain"], self._currentLanguage["popup"]["options"]["return"]], buttonCommands = [None, lambda event = None: self._paymentCancel(error = "")])

    def _paymentCancel(self, error = ""):
        self.paymentCancelEvent.set()
        subprocess.run(["pkill", "-9", "chromium-browse"])
        if error != "":
            self._logError(strError = error)
        else:
            self._success = NPSuccess(master = self._master, commands = [None, self._destroyCommand])
            self._success.place()
            self._payment.place_forget()

    def _generateQR(self):
        cost = str(self._userPrice)
        head_url="https://img.vietqr.io/image/" + PaymentAccount["bank"].strip() + "-" + PaymentAccount["accountNumber"].strip() + "-HgRYJqu.png?amount="
        tail_url="&addInfo=SSPS%20" + str(self._serverKey)
        if PaymentAccount["accountName"] != None:
            tail_url = tail_url + "&accountName=" + PaymentAccount["accountName"].strip().replace(" ", "%20")
        url=head_url+cost+tail_url
        try:
            urllib.request.urlretrieve(url, "GUI/Images/PaymentQR.png")
            self._payment.npset(attribute = "userQRFile", value = "GUI/Images/PaymentQR.png")
        except urllib.error.URLError:
            self._master.after(100, NPConfirmBox, self._master, self._currentLanguage["popup"]["error"]["lostConnection"], [None, "OK"], [None, lambda event = None: self._paymentCancel(error = self._currentLanguage["errorLog"]["message"]["errorLostConnection"])])
    
    def _paymentCheck(self): 
        try:
            googleUserInfo = "/home/pi/Desktop/NPPayCheck"
            option = webdriver.ChromeOptions()
            option.add_argument("user-data-dir=" + googleUserInfo)
            driver = Service('/usr/lib/chromium-browser/chromedriver')
            browser = webdriver.Chrome(service = driver, options = option)
            browser.get("https://mightytext.net/install")
            wait = WebDriverWait(browser, 100)

            # Login to Mighty Text Web
            for tries in range(0, 5):
                try:
                    wait.until(EC.element_to_be_clickable((By.ID, 'launch-webapp')))
                    login = browser.find_element(By.ID,'launch-webapp')
                    login.click()
                    break
                except:
                    pass

            for tries in range(0, 5):
                try:
                    original_window = browser.current_window_handle
                    wait.until(EC.number_of_windows_to_be(2))
                    for window_handle in browser.window_handles:
                        if window_handle != original_window:
                            browser.switch_to.window(window_handle)
                            break
                    break
        
                except:
                    pass

            # Check for web notification and close
            while True:
                try:
                    noti_list = browser.find_element(By.CLASS_NAME, 'intercom-post-close')
                except NoSuchElementException:
                    break
                for close_button in noti_list:
                    close_button.click()
            
            # Click to the message sent by OCB
            for tries in range(0, 5):
                try:
                    wait.until(EC.presence_of_element_located((By.ID, 'thread-78062')))
                    wait.until(EC.element_to_be_clickable((By.ID, 'thread-78062')))
                    click_ocb = browser.find_element(By.ID,'thread-78062')
                    click_ocb.click()
                    break
                except:
                    pass

            # Wait for new message
            sleep(10) 
            while True:
                if self.paymentCancelEvent.is_set():
                    return
                messageIndex = 0
                notFoundNewMessage = True
                while True:
                    messageIndex = messageIndex + 1
                    try:
                        messageList = browser.find_elements(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div[2]/div[' + str(messageIndex) + ']')
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
                messageStr = str(self._currentLanguage["errorLog"]["message"]["errorTransferAmount_1"]) + str(self._serverKey) + " (" + str(self._userPrice) + str(self._currentLanguage["errorLog"]["message"]["errorTransferAmount_2"]) + paymentStr + ")."
                self._master.after(100, NPConfirmBox, self._master, self._currentLanguage["popup"]["error"]["wrongTransferAmount"], [None, "OK"], [None, lambda event = None: self._paymentCancel(error = messageStr)])
        except Exception as e:
            try:
                if self.paymentCancelEvent.is_set() == False:
                    print(str(e))
                    self._master.after(100, NPConfirmBox, self._master, self._currentLanguage["popup"]["error"]["systemError"], [None, "OK"], [None, lambda event = None: self._paymentCancel(self._currentLanguage["errorLog"]["message"]["errorPaymentCheck"])])
            except Exception:
                return
    
    
    def _logError(self, strError):
        file_log = open("error_log.txt", "a")
        file_log.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " : " + strError + "\n")
        file_log.close()
        self._master.markErrorOccured()
    
    def _isPageLandscape(self, pageIndex, reader):
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

    def _printUserFile(self):
        reader = PdfReader("../CO3091_BE/user_file.pdf")
        # reader = PdfReader("./CO3091_BE/user_file.pdf") 
        
        def getFileSize():
            fileSize = self._format.npget(attribute = "filePaper")
            if (fileSize == "a3"):
                return "A3"
            if (fileSize == "a4"):
                return "A4"
            if (fileSize == "a5"):
                return "A5"

        def handlePrintError(strError, cfrmError):
            # Pause printing
            self.pauseEvent.set()
            self._printing.initControlButton(position = 'right', command = lambda event = None: self._adminPauseToPrint(), state = 'normal', text = self._currentLanguage["printing"]["control"]["continue"])
            
            # System to error state
            self._logError(strError = strError)

            NPConfirmBox(master = self._master, messageText = strError, buttonTexts = [None, "OK"], buttonCommands = [None, None])

        def getSideOption():
            sideOption = self._format.npget(attribute = "fileSides")
            if (sideOption == "1s"):
                return "one-sided"
            if (sideOption == "2s"):
                return "two-sided-" + self._fileFlip
        
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
                with open("../CO3091_BE/current_page.pdf", "wb") as fp:
                # with open("./CO3091_BE/current_page.pdf", "wb") as fp:
                    writer.write(fp)
                
                printerFile = open("printer.txt")
                printerName = printerFile.read().strip()
                printCommand = ["lp", "-d", printerName, "-o","media=" + getFileSize(), "-n", "1", "-o", "sides=" + getSideOption(), "-o", "fit-to-page"]
                if self._isPageLandscape(page, reader):
                    printCommand.extend(["-o", "landscape]"])
                printCommand.append("../CO3091_BE/current_page.pdf")
                # printCommand.append("./CO3091_BE/current_page.pdf")
                print(printCommand)
                
                try:
                    subprocess.run(printCommand, check = True)
                except subprocess.CalledProcessError as e:
                    self._master.after(100, handlePrintError, self._currentLanguage["errorLog"]["message"]["errorCritical"], self._currentLanguage["popup"]["error"]["systemError"])
                    return

                # Time out for error
                def printingTimeOut():
                    printer_status = subprocess.check_output(["lpstat", "-p", printerName]).decode().lower()
                    print(printer_status)
                    if (printer_status.find("idle") != -1):
                        pass
                    elif (printer_status.find("rendering completed") != -1):
                        handlePrintError(strError = self._currentLanguage["errorLog"]["message"]["errorCritical"], cfrmError = self._currentLanguage["popup"]["error"]["systemError"])
                    elif (printer_status.find("sending data to printer") != -1):
                        handlePrintError(strError = self._currentLanguage["errorLog"]["message"]["errorCritical"], cfrmError = self._currentLanguage["popup"]["error"]["systemError"])
                    else:
                        handlePrintError(strError = self._currentLanguage["errorLog"]["message"]["errorCritical"], cfrmError = self._currentLanguage["popup"]["error"]["systemError"])
                timeOutId = self._master.after(30000, printingTimeOut)
                isCommandError = False
                while True:
                    try:
                        printer_status = subprocess.check_output(["lpstat", "-p", printerName]).decode()
                    except subprocess.CalledProcessError as e:
                        self._master.after(100, handlePrintError, self._currentLanguage["errorLog"]["message"]["errorCritical"], self._currentLanguage["popup"]["error"]["systemError"])
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
        
