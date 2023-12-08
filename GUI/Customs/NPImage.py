from PIL import Image, ImageTk
from Customs.NPTheme import NPTheme

class NPImage:
    
    def __init__(self, file: str, width: int, height: int) -> None:
        
        self.width = int(width)
        self.height = int(height)
        
        currentTheme = NPTheme.getTheme()
        
        try:
            self.image = Image.open(file = file, mode = "r")
            self.image = self.image.resize(size = (self.width, self.height))
        except:
            self.image = Image.new(mode = "RGB", size = (self.width, self.height), color = currentTheme["color"])
            
        self.image = ImageTk.PhotoImage(image = self.image)