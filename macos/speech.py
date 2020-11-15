import wave
import pyaudio
import speech_recognition as sr
import subprocess
import datetime


voice = 'Tom'
speed = '160'


def set_voice(name: str):
    global voice
    voice = name


def get_voice():
    if voice == 'Tom':
        return "Jarvis"
    elif voice == "Samantha":
        return "Friday"


def set_speech_rate(rate):
    global speed
    speed = str(rate)


def speak(text):
    assistant = get_voice()

    print('\033[92m' + assistant + ':', text + '\033[0m')
    subprocess.call(['say', '-v', voice, '-r' + speed, text])


def get_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print('\033[94m' + 'You:', said + '\033[0m')
        except Exception as e:
            print(f"Exception: {e}")

    return said


def record():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    fs = 44100  # Record at 44100 samples per second
    seconds = 3

    date = datetime.datetime.now()
    filename = f"records/{str(date).replace(':', '-')}-record.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


# record()
