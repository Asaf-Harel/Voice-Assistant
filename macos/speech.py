import speech_recognition as sr
import subprocess

voice = 'Tom'


def set_voice(name: str):
    global voice
    voice = name


def get_voice():
    return voice


def speak(text):
    subprocess.call(['say', '-v', voice, '-r 160', text])


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
