import os
import speech_recognition as sr
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty(
        'voice', r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.setProperty('rate', 130)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print(f"Exception: {e}")

    return said.lower()
