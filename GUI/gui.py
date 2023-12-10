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
stt.initImage("w", "GUI/Images/Logo1.png")
stt.initImage("e", None)
stt.initText(400, "w", "Wakanda Forever")
stt.place()

# # Workspace
def tester():
    try:
        print(f1._format.npget("filePaper"))
        print(f1._format.npget("fileSides"))
    except:
        print("Fail")
    root.after(1000, tester)

from .Pages.Prints.NPPrints import NPPrints
f1 = NPPrints(root)

# fr = Frame(root)
# fr.place(x=0, y=0, width=800, height=480)
# from .Objects.NPButtonArray import NPButtonArray
# btns = NPButtonArray(fr, "multiple", 10, 10, 10, "nw", "red", 2, 3, 30, 30, None, [["default", "default", "active"], ["active", "disabled", "default"]])
# btns.place()

# Run the main application loop
root.mainloop()



