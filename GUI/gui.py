from tkinter import *

# Create the main application window
root = Tk()
root.geometry("600x600")
frame = Frame(root, background = "yellow")
frame.place(x=0, y=0, width=500, height=500)

from .Customs.NPTheme import NPTheme
NPTheme.setTheme("Default")
currentTheme = NPTheme.getTheme()
from .Customs.NPLanguage import NPLanguage
NPLanguage.setLanguage("Vietnamese")
currentLanguage = NPLanguage.getLanguage()

from .Objects.NPKeyBoard import NPKeyBoard
test0 = NPKeyBoard(frame, 10, 10, 10, "nw", "red", 50, "Hana", 8, "", entryFont = currentTheme["font"]["section"], inputFont = currentTheme["font"]["heading"], actionFont = currentTheme["font"]["small"])
test0.place()

# from Objects.NPButtonArray import NPButtonArray
# test0 = NPButtonArray(frame, "voting", 10, 10, 10, "nw", "red", 3, 3, 50, 40, currentTheme["font"]["strong"], [["disabled", "active", "default"], ["disabled", "active", "default"], ["disabled", "active", "default"]], [["A", "B", ""], ["", "", ""], ["", ""]])
# test0.place()

# Run the main application loop
root.mainloop()



