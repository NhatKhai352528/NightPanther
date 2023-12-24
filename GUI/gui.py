from .Systems.NPTk import NPTk
root = NPTk()
root.bind(sequence = "<Return>", func = lambda event = None: root.destroy())

from .Customs.NPTheme import NPTheme
<<<<<<< HEAD
NPTheme.setTheme(themeCode = 1)
# currentTheme = NPTheme.getTheme()
=======
NPTheme.setTheme(theme = "Default")
currentTheme = NPTheme.getTheme()
>>>>>>> 0e482ce (chore: change image)

from .Customs.NPLanguage import NPLanguage
NPLanguage.setLanguage(languageCode = 1)
# currentLanguage = NPLanguage.getLanguage()

from .Flows.NPFlows import NPFlows
flow = NPFlows(master = root)
flow.place()

def tester():
    try:
        print(flow._currentFlow)
        # print(flow._settings._primary._availableLanguages)
    except:
        print("Fail")
    root.after(1000, tester)
root.after(1000, tester)

root.mainloop()
