from tkinter.font import Font
import Customs.NPColor as NPColor
import Customs.NPFont as NPFont

Default = {
    "default": {
        "color": NPColor.Azure4,
        "size": 16
    },
    "font": {
        "default": Font(family = NPFont.Verdana, size = 16, weight = "normal", slant = "roman", underline = False, overstrike = False),
        "title": Font(family = NPFont.Verdana, size = 32, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "section": Font(family = NPFont.Verdana, size = 24, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "heading": Font(family = NPFont.Verdana, size = 20, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "strong": Font(family = NPFont.Verdana, size = 16, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "normal": Font(family = NPFont.Verdana, size = 16, weight = "normal", slant = "roman", underline = False, overstrike = False),
        "small": Font(family = NPFont.Verdana, size = 12, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "tiny": Font(family = NPFont.Verdana, size = 8, weight = "normal", slant = "italic", underline = False, overstrike = False)
    },
    "foreground": {
        "default": NPColor.Black0,
        "highlight": NPColor.Azure4,
        "inverse": NPColor.Black8
    },
    "background": {
        "default": NPColor.Black8,
        "interact": NPColor.Black7,
        "status": NPColor.Black1
    },
    "entry": {
        "default": NPColor.Black8,
        "select": NPColor.Azure4,
        "disabled": NPColor.Black8
    },
    "button": {
        "input": {
            "default": NPColor.Black3,
            "active": NPColor.Black2,
            "disabled": NPColor.Black6
        },
        "action": {
            "default": NPColor.Azure4,
            "active": NPColor.Azure3,
            "disabled": NPColor.Azure7
        },
        "select": {
            "default": NPColor.Black4,
            "active": NPColor.Azure3,
            "disabled": NPColor.Black6
        }
    },
    "progressBar": {
        "default": NPColor.Azure4,
        "filled": NPColor.Green4,
        "unfilled": NPColor.Black8
    }
}