from Customs.Themes.Default import Default
from Customs.Themes.Dark import Dark

class NPTheme:
    
    currentTheme = Default
    availableThemes = {"Default": Default, "Dark": Dark}
    
    @classmethod
    def setTheme(cls, theme: str = "defaultTheme"):
        if theme in cls.availableThemes:
            cls.currentTheme = cls.availableThemes[theme]
        else:
            cls.currentTheme = Default
            
    @classmethod
    def getTheme(cls):
        return cls.currentTheme