from PIL import Image, ImageTk
from ..Customs.NPTheme import NPTheme

currentTheme = NPTheme.getTheme()
        
class NPImage:
    
    def __init__(self, file: str, width: int, height: int) -> None:
        
        # Size variables
        self.width = int(width)
        self.height = int(height)
        
        try:
            self.image = Image.open(file = file, mode = "r")
            self.image = self.image.resize(size = (self.width, self.height))
        except:
            self.image = Image.new(mode = "RGB", size = (self.width, self.height), color = currentTheme["default"]["color"])
            
        self.image = ImageTk.PhotoImage(image = self.image)