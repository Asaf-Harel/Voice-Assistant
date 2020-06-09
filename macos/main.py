from google_calendar import authenticate_google, get_events, get_date
from speech import speak, get_audio, set_voice, get_voice
from search import search_google
from notes import note
from time import sleep, strftime
import subprocess

SERIVCE = authenticate_google()

CALENDAR_STRS = ["what do i have", "what do i do",
                 "do i have plans", "am i busy"]

NOTE_STRS = ["make a note", "write this down", "remember this", "note this"]

AGREEMENT_STRS = ["yes", "of course", "sure", "why not", "forever"]
DISAGREEMENT_STRS = ["no", "never", "quit", "go away", "exit"]

OPEN_STRS = ["open", "start", "execute", "launch"]

SEARCH_STRS = ["search for", "search to",
               "search", "look up", "look for", "look", "find out", "find", "what is", "investigate", "research for", "research"]
again = None

try:
    while True:
        print("Listening")
        text = get_audio()
        understand = False

        if get_voice() == "Tom":
            WAKE0 = "hello jarvis"
            WAKE1 = "hey jarvis"
            WAKE2 = "hi jarvis"
        elif get_voice() == "Samantha":
            WAKE0 = "hello friday"
            WAKE1 == "hey friday"
            WAKE2 == "hi friday"

        if text.count(WAKE0) > 0 or text.count(WAKE1) or text.count(WAKE2):
            speak("I am listening")

            while True:
                if again:
                    speak("Do you want something else?")
                    text = get_audio()
                    for phrase in DISAGREEMENT_STRS:
                        if phrase in text:
                            speak("OK goodbye sir")
                            again = False
                            break
                    for phrase in AGREEMENT_STRS:
                        if phrase in text:
                            speak("OK, what do you want?")
                            break

                    if not again:
                        break

                text = get_audio()

                if "hello" in text:
                    speak("hello, how are you today?")
                    understand = True

                elif "your" in text and "name" in text:
                    if get_voice() == "Tom":
                        speak("My name is Jarvis")
                    elif get_voice() == "Samantha":
                        speak("My name is Friday")
                    understand = True

                elif "who are you" == text or "tell me about you" == text:
                    if get_voice() == "Tom":
                        speak(
                            "My name is Jarvis, I was Iron man virtual assistant but one day i thought... damn Asaf is way smarter... so now I'm his assistant")
                    elif get_voice() == "Samantha":
                        speak(
                            "My name is Friday, I was Iron man virtual assistant but one day i thought... damn Asaf is way smarter... so now I'm his assistant")
                    understand = True

                elif "who is Asaf" in text:
                    speak("Asaf is the most smart man I've ever met")
                    understand == True

                elif "who is yuval" in text:
                    speak(
                        "Rader is a huge... I mean... giant... I mean... really really really really really big!... piece of shit")
                    understand = True

                elif "switch to friday" in text:
                    set_voice('Samantha')
                    speak("Hi sir, this is friday")
                    understand = True

                elif "switch to jarvis" in text:
                    set_voice('Tom')
                    speak("Hello sir, this is jarvis")
                    understand = True

                elif "time" in text:
                    speak(f"It's {strftime('%H:%M')} O'clock")
                    understand = True

                elif "date" in text:
                    speak(f"The date today is {strftime('%d-%m-%Y')}")
                    understand = True

                for phrase in CALENDAR_STRS:
                    if phrase in text:
                        date = get_date(text)
                        if date:
                            get_events(date, SERIVCE)
                        else:
                            speak("I couldn't understand the date")
                        understand = True

                for phrase in SEARCH_STRS:
                    if phrase in text:
                        search_google(text[len(phrase) + 1:])
                        understand = True
                        break

                for phrase in NOTE_STRS:
                    if phrase in text:
                        speak("What would you like me to write down?")
                        note_text = get_audio()
                        note(note_text)
                        speak("I've made a note of that.")
                        understand = True

                for phrase in OPEN_STRS:
                    if phrase in text:
                        app = list(text[len(phrase) + 1:])
                        app[0] = app[0].upper()
                        app = ''.join(app) + '.app'
                        print(app)
                        subprocess.call(['open', f'/Applications/{app}'])
                        understand = True

                if not understand:
                    speak("I didn't understand that")

                again = True
                understand = False
        sleep(0.2)

except:
    speak('Goodbye sir')
