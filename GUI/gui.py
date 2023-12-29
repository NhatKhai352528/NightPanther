from .Systems.NPTk import NPTk
root = NPTk()
root.bind(sequence = "<Return>", func = lambda event = None: root.destroy())

from .Customs.NPTheme import NPTheme
from .Customs.NPLanguage import NPLanguage
NPTheme.setTheme(themeCode = 1)
NPLanguage.setLanguage(languageCode = 1)

root.place()
root.mainloop()
