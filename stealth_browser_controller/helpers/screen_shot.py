import os
import datetime
import mss
import tempfile
import pyautogui
from collections import namedtuple
from typing import Optional
  
Point = namedtuple('Point', 'x y')

def take_screenshot(output_dir="."):
    """
    Takes a screenshot of the primary monitor and saves it as a PNG file.
    
    Args:
        output_dir (str): Directory where the screenshot will be saved. Defaults to current directory.
        
    Returns:
        str: Full path to the saved screenshot.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate timestamped filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(output_dir, f"screenshot_{timestamp}.png")
    
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # primary monitor
        screenshot = sct.grab(monitor)
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=filename)
    
    return filename

def locate_on_screen(image_path: str, confidence: float = 0.9) -> Optional[Point]:
    """
    Locates an image on the screen and returns its center coordinates.
    
    Args:
        image_path (str): Path to the image to locate.
        confidence (float): Confidence level for image matching.
        
    Returns:
        Point: Center coordinates of the located image, or None if not found.
    """
    temp_directory = tempfile.mkdtemp()
    screenshot_path = take_screenshot(temp_directory)
    result = pyautogui.locate(image_path, screenshot_path, confidence=confidence)
    os.remove(screenshot_path)
    if result is None:
        return None
    return pyautogui.center(result)