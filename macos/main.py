from google_calendar import authenticate_google, get_events, get_date
from speech import speak, get_audio, set_voice, get_voice, set_speech_rate
from search import search_google, search_imdb, search_movie
from notes import note
from device import turn_wifi, turn_bluetooth, set_volume, get_volume, set_brightness, get_brightness, notify, hide, quit, open_app
from time import sleep, strftime
import subprocess
import random

SERIVCE = authenticate_google()

GREETINGS = ['I am listening', 'Hello sir', 'what?!...... what?!...... whaaaaaaat?!?!', 'How can I help you?',
             'Really?... again?... what now?!', 'aye aye captain', "Oh hey, didn't see you there"]

GOODBYES = ['Goodbye sir', 'see ya later man',
            'Finally!... sayonara!', "That's it?!... bye bye"]

CALENDAR_STRS = ["what do i have", "what do i do",
                 "do i have plans", "am i busy", "do i do"]

NOTE_STRS = ["make a note", "write this down", "remember this", "note this"]

AGREEMENT_STRS = ["yes", "of course", "sure", "why not", "forever"]
DISAGREEMENT_STRS = ["no", "nope", "never", "quit", "go away", "exit"]

OPEN_STRS = ["open", "start", "execute", "launch", "show"]
MINIMIZE_STRS = ["minimize", "hide"]
QUIT_STRS = ["quit", "close"]

SEARCH_STRS = ["search for", "search", "look up", "look for", "look", "find out",
               "find", "what is", "investigate", "research for", "research about", "research"]

GENRES = ['action', 'adventure', 'animation', 'biography', 'comedy', 'crime', 'drama', 'family',
          'fantasy', 'history', 'horror', 'music', 'musical', 'mystery',
          'romance', 'sci-fi', 'sport', 'thriller', 'war', 'western']

again = None

try:
    while True:
        print("Listening")
        text = get_audio().lower()
        understand = False

        if get_voice() == "Jarvis":
            WAKE0 = "hello jarvis"
            WAKE1 = "hey jarvis"
            WAKE2 = "hi jarvis"
        elif get_voice() == "Friday":
            WAKE0 = "hello friday"
            WAKE1 == "hey friday"
            WAKE2 == "hi friday"

        if text.count(WAKE0) > 0 or text.count(WAKE1) or text.count(WAKE2):
            notify("Assistant Activated!")
            speak(random.choice(GREETINGS))

            while True:
                if again:
                    speak("Do you want something else?")
                    text = get_audio().lower()
                    for phrase in DISAGREEMENT_STRS:
                        if phrase in text:
                            speak(random.choice(GOODBYES))
                            again = False
                            break
                    for phrase in AGREEMENT_STRS:
                        if phrase in text:
                            speak("OK, what do you want?")
                            break

                    if not again:
                        break

                original_text = get_audio()
                text = original_text.lower()

                if "hello" in text:
                    speak("hello, how are you today?")
                    understand = True

                elif "your" in text and "name" in text:
                    if get_voice() == "Jarvis":
                        speak("My name is Jarvis")
                    elif get_voice() == "Friday":
                        speak("My name is Friday")
                    understand = True

                elif "who are you" == text or "tell me about you" == text:
                    if get_voice() == "Jarvis":
                        speak(
                            "My name is Jarvis, I was Iron man virtual assistant but one day i thought... damn Asaf is way smarter... so now I'm his assistant")
                    elif get_voice() == "Friday":
                        speak(
                            "My name is Friday, I was Iron man virtual assistant but one day i thought... damn Asaf is way smarter... so now I'm his assistant")
                    understand = True

                elif "who is Asaf" in text:
                    speak("Asaf is the most smart man I've ever met")
                    understand == True

                elif "switch to friday" in text:
                    set_voice('Samantha')
                    notify("Switched to Friday")
                    speak("Hi sir, this is friday")
                    understand = True

                elif "switch to jarvis" in text:
                    set_voice('Tom')
                    notify("Switched to Jarvis")
                    speak("Hello sir, this is jarvis")
                    understand = True

                elif "time" in text:
                    speak(f"It's {strftime('%H:%M')} O'clock")
                    understand = True

                elif "date" in text:
                    speak(f"The date today is {strftime('%d-%m-%Y')}")
                    understand = True

                elif "wi-fi" in text or "wifi" in text:
                    if "on" in text:
                        turn_wifi(True)
                        speak("Turned on Wi-Fi")
                        understand = True
                    elif "off" in text:
                        turn_wifi(False)
                        speak("Turned off Wi-Fi")
                        understand = True

                elif "bluetooth" in text:
                    if "on" in text:
                        turn_bluetooth(True)
                        speak("Turned bluetooth on!")
                        understand = True
                    elif "off" in text:
                        turn_bluetooth(False)
                        speak("Turned bluetooth off!")
                        understand = True

                elif "volume" in text or "speaker" in text:
                    if "to" in text:
                        for i in text.split():
                            if '%' in i:
                                i = i[:-1]
                            if i.isdigit():
                                num = int(i)
                                break
                        set_volume(num)
                        speak(f"Set volume to {num}%")
                        understand = True

                    if "increase" in text or "add" in text or "increment" in text or "raise" in text or "append" in text:
                        for i in text.split():
                            if '%' in i:
                                i = i[:-1]
                            if i.isdigit():
                                num = int(i)
                                if get_volume() != 0:
                                    volume = get_volume() + ((get_volume() * num) / 100)
                                    break
                                else:
                                    volume = num
                                    break
                        set_volume(volume)
                        speak(f"Increased volume by {num}%")
                        understand = True
                    elif "decrease" in text or "reduce" in text or "subtract" in text or "lower" in text:
                        for i in text.split():
                            if "%" in i:
                                i = i[:-1]
                            if i.isdigit():
                                num = int(i)
                                volume = get_volume() - ((get_volume() * num) / 100)
                                break
                        set_volume(volume)
                        speak(f"Decreased volume by {num}%")
                        understand = True

                elif "bright" in text:
                    if "set" in text:
                        for i in text.split():
                            if '%' in i:
                                i = i[:-1]
                            if i.isdigit():
                                num = float(i) / 100
                                set_brightness(num)
                                speak(f"Set brightness to {num * 100}%")
                                understand = True
                    elif "increase" in text or "add" in text or "increment" in text or "raise" in text or "append" in text:
                        for i in text.split():
                            if '%' in i:
                                i = i[:-1]
                            if i.isdigit():
                                num = int(i)
                                if get_brightness() != 0:
                                    brightness = get_brightness() + ((get_brightness() * num) / 100)
                                    break
                                else:
                                    brightness = num / 100
                                    break
                        set_brightness(brightness)
                        speak(f"Increased brightness by {num}%")
                        understand = True
                    elif "decrease" in text or "reduce" in text or "subtract" in text or "lower" in text:
                        for i in text.split():
                            if "%" in i:
                                i = i[:-1]
                            if i.isdigit():
                                num = int(i)
                                brightness = get_brightness() - ((get_brightness() * num) / 100)
                                break
                        set_brightness(brightness)
                        speak(f"Decreased brightness by {num}%")
                        understand = True

                for phrase in CALENDAR_STRS:
                    if phrase in text:
                        date = get_date(text)
                        if date:
                            get_events(date, SERIVCE)
                        else:
                            speak("I couldn't understand the date")
                        understand = True
                        break

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
                        break

                for phrase in OPEN_STRS:
                    if phrase in text:
                        try:
                            app = original_text[len(phrase) + 1:] + ".app"
                            if app[0].islower():
                                app = app[0].upper() + app[1:]
                            print(app)
                            open_app(app)
                        except:
                            break
                        notify(f"Opened {app.split('.')[0]}")
                        speak(f"Opened {app.split('.')[0]}")
                        understand = True
                        break

                for phrase in MINIMIZE_STRS:
                    if phrase in text:
                        try:
                            app = original_text[len(phrase) + 1:]
                            if app[0].islower():
                                app = app[0].upper() + app[1:]
                            print(app)
                            hide(app)
                        except:
                            break
                        notify(f"Hid {app}")
                        speak(f"Hid {app}")
                        understand = True
                        break

                for phrase in QUIT_STRS:
                    if phrase in text:
                        app = original_text[len(phrase) + 1:]
                        if app[0].islower():
                            app = app[0].upper() + app[1:]
                        if app == "":
                            break
                        print(app)
                        speak(f"Are you sure you want to close {app}?")
                        answer = get_audio().lower()
                        for agree in AGREEMENT_STRS:
                            if agree in answer:
                                quit(app)
                                notify(f"Closed {app}")
                                speak(f"Closed {app}")
                                break
                        understand = True
                        break

                for genre in GENRES:
                    if genre in text:
                        understand = True
                        movies = search_imdb(genre)
                        speak("Here is some new movies I've found")
                        understand = True
                        set_speech_rate(140)
                        for movie in movies:
                            speak(movie)
                        set_speech_rate(160)
                        speak("Would you like to hear more about them?")
                        answer = get_audio()
                        for phrase in AGREEMENT_STRS:
                            if phrase in answer:
                                speak("OK")
                                for movie in movies:
                                    details = search_movie(movie)
                                    speak(
                                        f"The movie {movie}, {details['runtime']} long, from {details['year']}, by {details['director']}, with the rate {details['rating']} is about {details['plot']}")
                        break

                if not understand:
                    notify("I didn't understand:", text)
                    speak("I didn't understand that")

                again = True
                understand = False
        sleep(0.1)

except:
    speak('Goodbye sir')
