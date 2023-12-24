from .Themes.Default import Default
from .Themes.Dark import Dark

class NPTheme:
    
    currentTheme = Default
    availableThemes = [Default, Dark]
    
    @classmethod
    def setTheme(cls, themeCode: int = None):
        try:
            cls.currentTheme = cls.availableThemes[themeCode]
        except:
            cls.currentTheme = cls.availableThemes[0]
            
    @classmethod
    def getTheme(cls):
        return cls.currentTheme
    
    @classmethod
    def getThemeIndex(cls):
        for i in range(len(cls.availableThemes)):
            if cls.currentTheme == cls.availableThemes[i]:
                return i