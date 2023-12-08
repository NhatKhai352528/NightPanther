from tkinter.font import Font
import Customs.NPColor as NPColor
import Customs.NPFont as NPFont

Dark = {
    "color": NPColor.Black1,
    "font": {
        "title": Font(family = NPFont.Verdana, size = 32, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "section": Font(family = NPFont.Verdana, size = 24, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "heading": Font(family = NPFont.Verdana, size = 20, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "strong": Font(family = NPFont.Verdana, size = 16, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "normal": Font(family = NPFont.Verdana, size = 16, weight = "normal", slant = "roman", underline = False, overstrike = False),
        "small": Font(family = NPFont.Verdana, size = 12, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "tiny": Font(family = NPFont.Verdana, size = 8, weight = "normal", slant = "italic", underline = False, overstrike = False)
    },
    "foreground": {
        "default": NPColor.Black8,
        "highlight": NPColor.Azure4,
        "inverse": NPColor.Black8
    },
    "background": {
        "default": NPColor.Black3,
        "interact": NPColor.Black2,
        "status": NPColor.Black1
    },
    "entry": {
        "default": NPColor.Black1,
        "select": NPColor.Azure3,
        "disabled": NPColor.Azure6
    },
    "inputButton": {
        "default": NPColor.Azure4,
        "active": NPColor.Azure3,
        "disabled": NPColor.Azure6
    },
    "actionButton": {
        "default": NPColor.Black3,
        "active": NPColor.Black2,
        "disabled": NPColor.Black6
    }
}