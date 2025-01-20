from stealth_browser_controller import StealthBrowserController
import time
import soundcard as sc
import soundfile as sf
import speech_recognition


def process_audio_challenge(wav_path: str = "output.wav") -> str:
    """Process the audio challenge and return the recognized text.

    Args:
        audio_url: URL of the audio file to process

    Returns:
        str: Recognized text from the audio file
    """

    recognizer = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(wav_path) as source:
        audio = recognizer.record(source)

        return recognizer.recognize_google(audio)


def record_system_audio(duration=10, samplerate=48000, output_file="output.wav"):
    """
    Record system audio for a specified duration.

    Args:
        duration (int): Recording duration in seconds (default: 5)
        samplerate (int): Sample rate in Hz (default: 48000)
        output_file (str): Output file name/path (default: 'output.wav')

    Returns:
        bool: True if recording was successful, False otherwise
    """

    loopback = sc.get_microphone(
        id=str(sc.default_speaker().name), include_loopback=True
    )

    numframes = samplerate * duration

    print(f"Recording system audio for {duration} seconds...")
    with loopback.recorder(samplerate=samplerate) as mic:
        data = mic.record(numframes=numframes)
    print("Recording finished.")

    sf.write(output_file, data, samplerate)
    print(f"System audio saved as {output_file}")

    return True


# Example usage
def main():
    params = []
    browser = StealthBrowserController("google-chrome") # enter path of the browser here
    browser.open("https://www.google.com/recaptcha/api2/demo")
    time.sleep(10)
    ele = browser.find_element_by_image("imgs/1.png")
    print(ele.x, ele.y)
    ele.click()

    is_solved = bool(browser.find_element_by_image("imgs/x.png", timeout=1))
    if is_solved:
        print("Captcha solved when clicking the element")
        return
    else:
        print("Captcha not solved when clicking the element")
        print("Attempting to solve captcha by recording system audio")

    ele2 = browser.find_element_by_image("imgs/2.png")
    ele2.click()
    time.sleep(5)

    ele3 = browser.find_element_by_image("imgs/3.png")
    ele3.click()
    record_system_audio()
    text = process_audio_challenge()
    print(text)
    ele4 = browser.find_element_by_image("imgs/4.png")
    ele4.click()
    ele4.input_text(text)
    ele5 = browser.find_element_by_image("imgs/5.png")
    ele5.click()

    is_solved = bool(browser.find_element_by_image("imgs/x.png", timeout=1))
    if is_solved:
        print("Captcha solved when typing the text")
    else:
        print("Captcha not solved when typing the text")

    input("Press Enter to continue...")
    browser.close()


if __name__ == "__main__":
    main()
