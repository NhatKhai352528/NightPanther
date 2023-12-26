from .Languages.English import English
from .Languages.Vietnamese import Vietnamese

class NPLanguage:
    
    currentLanguage = English
    availableLanguages = [English, Vietnamese]
            
    @classmethod
    def setLanguage(cls, languageCode: int = None):
        try:
            cls.currentLanguage = cls.availableLanguages[languageCode]
        except:
            cls.currentLanguage = cls.availableLanguages[0]
            
    @classmethod
    def getLanguage(cls):
        return cls.currentLanguage
    
    @classmethod
    def getLanguageIndex(cls):
        for i in range(len(cls.availableLanguages)):
            if cls.currentLanguage == cls.availableLanguages[i]:
                return i