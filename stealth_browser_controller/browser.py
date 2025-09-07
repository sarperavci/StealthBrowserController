from typing import Optional, Tuple
import subprocess
import pyautogui
import time
from .models.element import Element
from .helpers.mouse_controller import get_mouse
from .helpers.screen_shot import locate_on_screen

class StealthBrowserController:
    """Main controller class for browser automation"""

    def __init__(
        self, browser_path: Optional[str] = None, params: Optional[list] = None
    ):
        self.browser_path = browser_path
        self._process = None
        self.params = params
        self.mouse_controller = get_mouse()

    def open(self, url: str, wait_time: int = 2, max_retries: int = 3) -> bool:
        """
        Open a URL in the browser with improved error handling and verification.

        Args:
            url (str): The URL to open
            wait_time (int): Time to wait for browser to load in seconds (default: 2)
            max_retries (int): Maximum number of retry attempts (default: 3)

        Returns:
            bool: True if browser opened successfully, False otherwise
        """
        if not self.browser_path:
            raise ValueError("Browser path not set")

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        args = [self.browser_path]
        if self.params:
            args.extend(self.params)
        args.append(url)

        for attempt in range(max_retries):
            try:
                if self._process:
                    self.close()

                self._process = subprocess.Popen(
                    args,
                    stderr=subprocess.DEVNULL,
                    stdout=subprocess.DEVNULL,
                    start_new_session=True,
                )

                time.sleep(wait_time)

                return True

            except subprocess.SubprocessError as e:
                print(f"Failed to open browser on attempt {attempt + 1}: {str(e)}")
                if attempt < max_retries - 1:
                    time.sleep(1)
                    continue

        print("Failed to open browser after all attempts")
        return False

    def close(self):
        """Close the browser"""
        self._process.terminate()
        self._process = None

    def find_element_by_image(
        self, image_path: str, timeout: int = 10, confidence: float = 0.9
    ) -> Optional[Element]:
        """Find an element on screen by matching an image"""
        t0 = time.time()
        while time.time() - t0 < timeout:
            try:
                location = locate_on_screen(image_path, confidence=confidence)
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
