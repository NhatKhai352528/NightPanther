from ...Constants.NPPaperPrice import PaperPrice
from ...Constants.NPInkPrice import InkPrice

def setPaperPrice(paper, price):
    PaperPrice[paper] = price
    with open("GUI/Constants/NPPaperPrice.py", "w") as file:
        file.write("PaperPrice = " + repr(PaperPrice))

def setInkPrice(paper, price):
    InkPrice[paper] = price
    with open("GUI/Constants/NPInkPrice.py", "w") as file:
        file.write("InkPrice = " + repr(InkPrice))
