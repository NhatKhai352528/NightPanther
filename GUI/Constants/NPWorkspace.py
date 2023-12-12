from .NPScreen import Viewport, Menu

Data = {
    "x": 0,
    "y": int(Menu["y"] + Menu["height"]),
    "width": int(0.4 * Viewport["width"]),
    "height": int(0.6 * Viewport["height"]),
    "distance": int(Viewport["distance"])
}

Control = {
    "x": 0,
    "y": int(Data["y"] + Data["height"]),
    "width": int(0.4 * Viewport["width"]),
    "height": int(0.2 * Viewport["height"]),
    "distance": int(Viewport["distance"])
}

Interact = {
    "x": int(Menu["x"] + Menu["width"]),
    "y": int(Menu["y"]),
    "width": int(0.6 * Viewport["width"]),
    "height": int(Viewport["height"]),
    "distance": int(Viewport["distance"])
}