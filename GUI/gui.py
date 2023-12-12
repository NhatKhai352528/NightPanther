from .Systems.NPTk import NPTk
root = NPTk()
root.bind(sequence = "<Return>", func = lambda event = None: root.destroy())

from .Customs.NPTheme import NPTheme
NPTheme.setTheme("Default")
currentTheme = NPTheme.getTheme()

from .Customs.NPLanguage import NPLanguage
NPLanguage.setLanguage("English")
currentLanguage = NPLanguage.getLanguage()

from .Flows.NPFlows import NPFlows
q3 = NPFlows(root)
q3.place()

def tester():
    try:
        print(q3._currentFlow)
    except:
        print("Fail")
    root.after(1000, tester)
root.after(100, tester)

root.mainloop()
