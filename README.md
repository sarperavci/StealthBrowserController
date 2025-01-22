# Stealth Browser Controller 🕵️‍♂️

Feeling insecure using Selenium, playwright, puppeteer, etc? Let's make things simple.

A Python package for browser automation that mimics human-like behavior with natural mouse movements and realistic typing patterns without using any browser automation libraries.

## 🌟 Features

- Human-like mouse movements and clicks
- Natural typing patterns
- Image-based element detection
- Easy-to-use browser control

## 🚀 Installation

```bash
pip install stealth-browser-controller
```

## 🎮 Quick Start

```python
from stealth_browser_controller import StealthBrowserController

# Create a browser instance
browser = StealthBrowserController("google-chrome")
# browser = StealthBrowserController("path/to/your/browser/executable")

# Open a website
browser.open("https://www.google.com")

# Find an element by image and input text
search_input = browser.find_element_by_image("path/to/search_input.png")
if search_input:
    search_input.input_text("Hello, World!")

# Find an element by image and click it
search_button = browser.find_element_by_image("path/to/search_button.png")
if search_button:
    search_button.click()
# Close the browser
browser.close()
```

## 📚 Documentation

### Browser Class
The main class for controlling the browser. Supports:
- Opening URLs
- Finding elements by image
- Typing text
- Mouse movements
- Scrolling
- Key presses

### Element Class
Represents elements on the page. Supports:
- Clicking (single, double, right-click)
- Text input
- Visibility checking

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.