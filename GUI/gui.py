from tkinter import *

# Create the main application window
root = Tk()
root.geometry("800x480")
from .Customs.NPTheme import NPTheme
NPTheme.setTheme("Default")
currentTheme = NPTheme.getTheme()
from .Customs.NPLanguage import NPLanguage
NPLanguage.setLanguage("English")
currentLanguage = NPLanguage.getLanguage()

# Status
from .Frames.NPStatus import NPStatus
stt = NPStatus(root)
stt.initImage("w", None)
stt.initImage("e", None)
stt.initText(200, "w", "Rang ai di qua quan doc")
stt.place()

# Worksapce frame
from .Frames.Workspaces.NPWorkspace import NPWorkspace
ws = NPWorkspace(root)
frame = ws.npget("frame")
ws.place()

# Menu
from .Frames.Workspaces.NPMenu import NPMenu
mn = NPMenu(frame)
mn.initButton(0, None, None, "normal")
mn.initButton(1, None, None, "normal")
mn.initButton(2, None, None, "normal")
mn.initButton(3, None, None, "disabled")
mn.place()

# Control
from .Frames.Workspaces.NPControl import NPControl
ctr = NPControl(frame)
ctr.initButton("left", None, "normal", "Yoooo")
ctr.initButton("right", None, "normal", "Yaaa")
ctr.place()

from .Frames.Workspaces.NPData import NPData
test2 = NPData(frame)
index0 = test2.initText("title", "Trong khong gian bay bay", False)
index0 = test2.initText("Heading", "Mot hanh tinh than ai", False)
index0 = test2.initText("heading", "Mot loi me ru con", True)
index0 = test2.initText("Content", "Binh yen giac say", True)
index0 = test2.initText("heading", "Mot dan chim tung canh", True)
index0 = test2.initText("content", "Don may troi hien lanh", True)
test2.place()

# Interact

def tester():
    try:
        ws.destroy()
    except:
        print("Kitchen")
def testor():
    try:
        print("Testor")
    except:
        print("Kitchen")
    root.after(1000, testor)

from .Frames.Workspaces.NPInteract import NPInteract
test15 = NPInteract(frame)
# test15.initText("heading", "Mot con vit xoe", "center")
# test15.initText("content", "", "center")
# idx17 = test15.initKeyBoard()
# idx16 = test15.initImage("GUI/Images/Logo1.png", 300, 300)
# idx15 = test15.initButtonArray("single", 10, 10, 20, 20, [["default", "default", "default"], ["default", "default", "default"], ["default", "default", "default"]], [["", "", ""], ["", "", ""], ["", "", ""]])
idx14 = test15.initProgressBar(0, 0)
idx13 = test15.initSpinBox(0, 0, 20, 1, True, "Hello", lambda event = None: tester())
test15.place()

# from .Objects.NPKeyBoard import NPKeyBoard
# test1 = NPKeyBoard(test2._frame, 10, 10, 10, "nw", "red", 50, "Hana", 8, "", entryFont = currentTheme["font"]["section"], inputFont = currentTheme["font"]["heading"], actionFont = currentTheme["font"]["small"])
# test1.place()

# from .Objects.NPButtonArray import NPButtonArray
# test0 = NPButtonArray(frame, "voting", 10, 10, 10, "nw", "red", 3, 3, 50, 40, currentTheme["font"]["strong"], [["disabled", "active", "default"], ["disabled", "active", "default"], ["disabled", "active", "default"]], [["A", "B", ""], ["", "", ""], ["", ""]])
# test0.place()

# Run the main application loop
root.mainloop()



