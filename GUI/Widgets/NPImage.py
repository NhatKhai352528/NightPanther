from PIL import Image
from PIL.ImageTk import PhotoImage
from ..Customs.NPTheme import NPTheme

currentTheme = NPTheme.getTheme()
        
class NPImage(PhotoImage):
    
    def __init__(self, file: str, width: int, height: int):
        
        # File path
        self._file = file
        
        # Size variables
        self._width = int(width)
        self._height = int(height)
        
        try:
            self._image = Image.open(fp = self._file, mode = "r")
            self._image = self._image.resize(size = (self._width, self._height))
        except:
            self._image = Image.new(mode = "RGB", size = (self._width, self._height), color = currentTheme["default"]["color"])
        
        super().__init__(image = self._image)