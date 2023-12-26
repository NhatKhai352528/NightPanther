from tkinter.font import Font
from ..Colors.BasicRGB import BasicRGB
from ..Colors.IBM import IBM
from ..Fonts.BasicFont import BasicFont

Dark = {
    "default": {
        "color": IBM["gray"]["default"]["10"],
        "size": 16,
    },
    "font": {
        "default": Font(family = BasicFont["verdana"], size = 16, weight = "normal", slant = "roman", underline = False, overstrike = False),
        "title": Font(family = BasicFont["verdana"], size = 28, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "section": Font(family = BasicFont["verdana"], size = 24, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "heading": Font(family = BasicFont["verdana"], size = 20, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "strong": Font(family = BasicFont["verdana"], size = 16, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "normal": Font(family = BasicFont["verdana"], size = 16, weight = "normal", slant = "roman", underline = False, overstrike = False),
        "small": Font(family = BasicFont["verdana"], size = 12, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "tiny": Font(family = BasicFont["verdana"], size = 8, weight = "normal", slant = "italic", underline = False, overstrike = False),
    },
    "foreground": {
        "default": IBM["gray"]["default"]["10"],
        "highlight": IBM["blue"]["default"]["30"],
        "inverse": BasicRGB["white"]["0"],
    },
    "background": {
        "default": IBM["gray"]["default"]["100"],
        "workspace": IBM["gray"]["default"]["80"], 
        "menu": IBM["gray"]["default"]["90"],
        "data": IBM["gray"]["default"]["100"],
        "interact": IBM["gray"]["default"]["80"],
        "control": IBM["gray"]["default"]["90"],
        "status": IBM["gray"]["default"]["100"],
        "confirm": IBM["gray"]["default"]["70"],
    },
    "entry": {
        "default": IBM["gray"]["default"]["100"],
        "select": IBM["gray"]["default"]["100"],
        "disabled": IBM["gray"]["default"]["100"],
    },
    "button": {
        "input": {
            "default": IBM["gray"]["default"]["60"],
            "active": IBM["gray"]["default"]["100"],
            "disabled": IBM["gray"]["default"]["70"],
        },
        "action": {
            "default": IBM["blue"]["default"]["60"],
            "active": IBM["blue"]["default"]["70"],
            "disabled": IBM["gray"]["default"]["60"],
        },
        "select": {
            "default": IBM["blue"]["default"]["30"],
            "active": IBM["blue"]["default"]["60"],
            "disabled": IBM["gray"]["default"]["70"],
        }
    },
    "progressBar": {
        "default": IBM["gray"]["default"]["70"],
        "filled": IBM["blue"]["default"]["60"],
        "unfilled": IBM["gray"]["default"]["60"],
    },
    "menuBar": {
        "reset": "./GUI/Images/Home-modified.png",
        "help": "./GUI/Images/Help-modified.png",
        "setting": "./GUI/Images/Construct-modified.png",
        "admin": "./GUI/Images/Account-modified.png",
    }
}