import human_mouse


mouse = None
def get_mouse() -> human_mouse.MouseController:
    global mouse
    if mouse is None:
        mouse = human_mouse.MouseController()
    return mouse