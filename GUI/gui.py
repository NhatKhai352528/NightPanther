from tkinter import *

# Create the main application window
root = Tk()
root.geometry("800x480")
from .Customs.NPTheme import NPTheme
NPTheme.setTheme("Default")
currentTheme = NPTheme.getTheme()
from .Customs.NPLanguage import NPLanguage
NPLanguage.setLanguage("Vietnamese")
currentLanguage = NPLanguage.getLanguage()

# Status
from .Frames.NPStatus import NPStatus
stt = NPStatus(root)
stt.initImage("w", None)
stt.initImage("e", None)
stt.initText(400, "w", "Wakanda Forever")
stt.place()

# Workspace
def tester():
    try:
        pass
    except:
        print("Fail")

from .Pages.Prints.NPPrints import NPPrints
NPPrints(root)

# from .Pages.Prints.NPFormat import NPFormat
# pg12 = NPFormat(root)
# pg12.place()
# root.after(2000, tester)

# Run the main application loop
root.mainloop()



