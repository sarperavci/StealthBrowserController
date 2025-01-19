from typing import Optional, Tuple
import subprocess
import pyautogui
import time
from .models.element import Element


class StealthBrowserController:
    """Main controller class for browser automation"""
    def __init__(self, browser_path: Optional[str] = None, params: Optional[list] = None):
        self.browser_path = browser_path
        self._process = None
        self.params = params
    
    def open(self, url: str):
        """Open a URL in the browser"""
        self._process = subprocess.Popen([self.browser_path, url], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        time.sleep(2)
    
    def close(self):
        """Close the browser"""
        self._process.terminate()
        self._process = None
    
    def find_element_by_image(self, image_path: str, timeout: int = 10) -> Optional[Element]:
        """Find an element on screen by matching an image"""
        t0 = time.time()
        while time.time() - t0 < timeout:
            try:
                location = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)
                if location:
                    return Element(image_path, location.x, location.y)
            except pyautogui.ImageNotFoundException:
                pass
        return None
    
    def type_text(self, text: str):
        """Type text at current cursor position"""
        pyautogui.typewrite(text)
    
    def press_key(self, key: str):
        """Press a specific key"""
        pyautogui.press(key)
    
    def scroll(self, amount: int):
        """Scroll the page. Positive values scroll up, negative scroll down"""
        pyautogui.scroll(amount)
    
    def get_mouse_position(self) -> Tuple[int, int]:
        """Get current mouse position"""
        return pyautogui.position()
    
    def move_to(self, x: int, y: int):
        """Move mouse to specific coordinates"""
        pyautogui.moveTo(x, y)
