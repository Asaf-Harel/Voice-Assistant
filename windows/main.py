from google_calendar import authenticate_google, get_events, get_date
from speech import speak, get_audio
from notes import note
from time import sleep

WAKE = "hello friday"

SERIVCE = authenticate_google()

CALENDAR_STRS = ["what do i have", "what do i do",
                 "do i have plans", "am i busy"]
NOTE_STRS = ["make a note", "write this down", "remember this"]

AGREEMENT_STRS = ["yes", "of course", "sure", "why not", "forever"]
DISAGREEMENT_STRS = ["no", "never", "quit", "go away"]

again = None

while True:
    print("Listening")
    text = get_audio()

    if text.count(WAKE) > 0:
        speak("I am listening")

        while True:
            if again:
                speak("Do you want something else?")
                text = get_audio()
                for phrase in DISAGREEMENT_STRS:
                    if phrase in text:
                        speak("OK goodbye")
                        again = False
                        break
                for phrase in AGREEMENT_STRS:
                    if phrase in text:
                        speak("OK, what do you want?")
                        break

                if not again:
                    break

            text = get_audio()

            for phrase in CALENDAR_STRS:
                if phrase in text:
                    date = get_date(text)
                    if date:
                        get_events(date, SERIVCE)
                    else:
                        speak("I didn't understand what you said, please try again")

            for phrase in NOTE_STRS:
                if phrase in text:
                    speak("What would you like me to write down?")
                    note_text = get_audio()
                    note(note_text)
                    speak("I've made a note of that.")

            if "hello" in text:
                speak("hello, how are you today?")

            if "what is your name" in text:
                speak("My name is Friday")

            if "who are you" in text:
                speak("My name is Friday, I was Iron man virtual assistant but one day i thought... damn Asaf is way smarter... so now I'm his assistant")

            if "who is yuval" in text:
                speak(
                    "Rader is a huge... I mean... giant... I mean... really really really really really BIG! piece of shit")
            else:
                speak("I didn't understand that")
            again = True
    sleep(0.2)
