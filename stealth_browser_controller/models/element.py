import human_mouse
import pyautogui
from ..helpers.mouse_controller import get_mouse


class Element:
    """Base class for browser elements like buttons, inputs, links etc."""

    _mouse: human_mouse.MouseController

    def __init__(
        self, image_path: str, x: int, y: int, mouse: human_mouse.MouseController = None
    ):
        self.image_path = image_path
        self.x = x
        self.y = y
        self._mouse = mouse or get_mouse()

    def click(self):
        """Click on the element"""
        self._mouse.perform_click(self.x, self.y)

    def double_click(self):
        """Double click on the element"""
        self._mouse.perform_double_click(self.x, self.y)

    def right_click(self):
        """Right click on the element"""
        self._mouse.move_to(self.x, self.y)
        pyautogui.rightClick()

    def input_text(self, text: str, delay: float = 0.05):
        """Input text into the element"""
        self._mouse.perform_click(self.x, self.y)
        pyautogui.typewrite(text, interval=delay)

    def is_visible(self) -> bool:
        """Check if the element is visible"""
        try:
            pyautogui.locateCenterOnScreen(self.image_path, confidence=0.9)
            return True
        except pyautogui.ImageNotFoundException:
            return False
