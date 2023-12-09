from tkinter import Tk
from ..NPFrames import NPFrames
from ...Constants.NPScreen import Workspace
from ...Customs.NPTheme import NPTheme

currentTheme = NPTheme.getTheme()

class NPWorkspace(NPFrames):
    
    def __init__(self, master: Tk):
        
        super().__init__(master = master, x = Workspace["x"], y = Workspace["y"], width = Workspace["width"], height = Workspace["height"], distance = Workspace["distance"], anchor = "nw", background = currentTheme["background"]["workspace"])
