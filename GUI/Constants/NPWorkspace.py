from .NPScreen import Workspace

Menu = {
    "x": 0,
    "y": 0,
    "width": int(0.4 * Workspace["width"]),
    "height": int(0.2 * Workspace["height"]),
    "distance": int(Workspace["distance"])
}

Data = {
    "x": 0,
    "y": int(Menu["y"] + Menu["height"]),
    "width": int(0.4 * Workspace["width"]),
    "height": int(0.6 * Workspace["height"]),
    "distance": int(Workspace["distance"])
}

Control = {
    "x": 0,
    "y": int(Data["y"] + Data["height"]),
    "width": int(0.4 * Workspace["width"]),
    "height": int(0.2 * Workspace["height"]),
    "distance": int(Workspace["distance"])
}

Interact = {
    "x": int(Menu["x"] + Menu["width"]),
    "y": int(Menu["y"]),
    "width": int(0.6 * Workspace["width"]),
    "height": int(Workspace["height"]),
    "distance": int(Workspace["distance"])
}