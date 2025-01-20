# Stealth Browser Controller Demo

A demonstration of automated reCAPTCHA solving using image recognition and system audio recording, powered by the `stealth-browser-controller` library.

## Overview

This demo showcases an alternative approach to solving reCAPTCHA challenges without traditional browser automation APIs like Selenium. Instead, it uses screen-based element detection and system audio recording.

## How it Works

The automation process follows these steps:

1. Locates and clicks the reCAPTCHA checkbox using image recognition
2. If human verification is required:
   - Switches to audio challenge mode
   - Records system audio during challenge playback
   - Uses speech recognition to convert audio to text
   - Submits the transcribed answer

## Element Detection

The demo uses the following reference images to locate and interact with reCAPTCHA elements:

![reCAPTCHA Checkbox](imgs/1.png)
*Initial checkbox to start the challenge*

![Audio Challenge Button](imgs/2.png)
*Button to switch to audio challenge mode*

![Play Button](imgs/3.png)
*Button to play the audio challenge*

![Answer Input Field](imgs/4.png)
*Text field for submitting the transcribed answer*

![Submit Button](imgs/5.png)
*Button to submit the answer*

![Success Indicator](imgs/x.png)
*Image used to verify successful completion*

## Demo Video

Here you can see the demo video:

https://github.com/user-attachments/assets/2c2993b9-25b9-4576-92a1-505b04125c0f

