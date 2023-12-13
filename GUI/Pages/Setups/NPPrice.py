from ...Constants.NPPrice import Price

def setPrice(paper, side, price):
    Price[paper][side] = price
    with open("GUI/Constants/NPPrice.py", "w") as file:
        file.write("Price = " + repr(Price))
