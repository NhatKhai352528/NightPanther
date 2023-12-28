from .Systems.NPTk import NPTk
root = NPTk()
root.bind(sequence = "<Return>", func = lambda event = None: root.destroy())

from .Customs.NPTheme import NPTheme
NPTheme.setTheme(themeCode = 1)

from .Customs.NPLanguage import NPLanguage
NPLanguage.setLanguage(languageCode = 1)

root.resetFlows()

def tester():
    try:
        print(root._flows._currentFlow)
    except:
        print("Fail")
    root.after(1000, tester)
#root.after(1000, tester)

root.mainloop()
