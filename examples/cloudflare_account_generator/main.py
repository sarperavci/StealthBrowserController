from stealth_browser_controller import StealthBrowserController
import os

def main():
    email = f"your_email{os.urandom(5).hex()}@gmail.com"
    password = "V3ryS3cur3P@ssw0rd"
    browser = StealthBrowserController("firefox")

    browser.open("https://dash.cloudflare.com/sign-up")

    browser.find_element_by_image("imgs/1.png", timeout=60).click()

    browser.find_element_by_image("imgs/2.png", timeout=60).input_text(email)
    browser.find_element_by_image("imgs/x.png", timeout=60).click()

    browser.find_element_by_image("imgs/3.png", timeout=60).input_text(password)

    browser.find_element_by_image("imgs/4.png", timeout=60).click()

    input("Press Enter to continue...")


if __name__ == "__main__":
    main()
