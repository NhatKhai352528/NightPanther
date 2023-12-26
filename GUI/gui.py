from .Systems.NPTk import NPTk
root = NPTk()
root.bind(sequence = "<Return>", func = lambda event = None: root.destroy())

from .Customs.NPTheme import NPTheme
NPTheme.setTheme(themeCode = 1)

from .Customs.NPLanguage import NPLanguage
NPLanguage.setLanguage(languageCode = 1)

from .Flows.NPFlows import NPFlows
flow = NPFlows(master = root)
flow.place()

def tester():
    try:
        print(flow._currentFlow)
    except:
        print("Fail")
    root.after(1000, tester)
root.after(1000, tester)

root.mainloop()
