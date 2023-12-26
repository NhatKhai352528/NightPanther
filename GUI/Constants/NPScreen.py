Screen = {
    "x": 0,
    "y": 0,
    "width": 800,
    "height": 480,
    "distance": 10
}

Status = {
    "x": 0,
    "y": 0,
    "width": int(Screen["width"]),
    "height": int(0.1 * Screen["height"]),
    "distance": int(Screen["distance"])
}

Viewport = {
    "x": 0,
    "y": int(Status["height"]),
    "width": int(Screen["width"]),
    "height": int(0.9 * Screen["height"]),
    "distance": int(Screen["distance"])
}

Menu = {
    "x": 0,
    "y": int(Viewport["y"]),
    "width": int(0.4 * Viewport["width"]),
    "height": int(0.2 * Viewport["height"]),
    "distance": int(Viewport["distance"])
}