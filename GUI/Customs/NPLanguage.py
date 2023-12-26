from .Languages.English import English
from .Languages.Vietnamese import Vietnamese

class NPLanguage:
    
    currentLanguage = English
    availableLanguages = {"English": English, "Vietnamese": Vietnamese}
    
    @classmethod
    def setLanguage(cls, language: str = "English"):
        if language in cls.availableLanguages:
            cls.currentLanguage = cls.availableLanguages[language]
        else:
            cls.currentLanguage = English
            
    @classmethod
    def getLanguage(cls):
        return cls.currentLanguage
    
    @classmethod
    def getLanguages(cls):
        return list(cls.availableLanguages.keys())