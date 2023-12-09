from tkinter.font import Font
from ..Colors.BasicRGB import BasicRGB
from ..Fonts.BasicFont import BasicFont

Dark = {
    "default": {
        "color": BasicRGB["azure"]["4"],
        "size": 16,
    },
    "font": {
        "default": Font(family = BasicFont["verdana"], size = 16, weight = "normal", slant = "roman", underline = False, overstrike = False),
        "title": Font(family = BasicFont["verdana"], size = 32, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "section": Font(family = BasicFont["verdana"], size = 24, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "heading": Font(family = BasicFont["verdana"], size = 20, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "strong": Font(family = BasicFont["verdana"], size = 16, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "normal": Font(family = BasicFont["verdana"], size = 16, weight = "normal", slant = "roman", underline = False, overstrike = False),
        "small": Font(family = BasicFont["verdana"], size = 12, weight = "bold", slant = "roman", underline = False, overstrike = False),
        "tiny": Font(family = BasicFont["verdana"], size = 8, weight = "normal", slant = "italic", underline = False, overstrike = False),
    },
    "foreground": {
        "default": BasicRGB["white"]["0"],
        "highlight": BasicRGB["azure"]["4"],
        "inverse": BasicRGB["black"]["0"],
    },
    "background": {
        "default": BasicRGB["black"]["3"],
        "status": BasicRGB["black"]["1"],
        "workspace": BasicRGB["black"]["3"],
        "menu": BasicRGB["black"]["3"],
        "data": BasicRGB["black"]["3"],
        "control": BasicRGB["black"]["3"],
        "interact": BasicRGB["black"]["2"],
    },
    "entry": {
        "default": BasicRGB["white"]["0"],
        "select": BasicRGB["azure"]["4"],
        "disabled": BasicRGB["white"]["0"],
    },
    "button": {
        "input": {
            "default": BasicRGB["black"]["3"],
            "active": BasicRGB["black"]["2"],
            "disabled": BasicRGB["white"]["2"],
        },
        "action": {
            "default": BasicRGB["azure"]["4"],
            "active": BasicRGB["azure"]["3"],
            "disabled": BasicRGB["azure"]["7"],
        },
        "select": {
            "default": BasicRGB["black"]["4"],
            "active": BasicRGB["azure"]["3"],
            "disabled": BasicRGB["white"]["2"],
        }
    },
    "progressBar": {
        "default": BasicRGB["azure"]["4"],
        "filled": BasicRGB["green"]["4"],
        "unfilled": BasicRGB["white"]["0"],
    }
}