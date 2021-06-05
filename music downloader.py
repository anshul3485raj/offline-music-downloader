from youtube_dl import YoutubeDL
from requests import get
import pyttsx3
import speech_recognition as sr
from PyDictionary import PyDictionary
dictionary = PyDictionary()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audioo):
    engine.say(audioo)
    engine.runAndWait()
def song(link):

    options = {
        'format': 'aac/mp3/ogg/wav/3gp/m4a/mp4',
        'outtmpl': 'downloads/%(title)s.mp3',
        'quiet': 'True'
    }
    with YoutubeDL(options) as ydl:
        try:
            get(link)
        except:
            metadata = ydl.extract_info(f"ytsearch:{link}", download=True)['entries'][0]
        else:
            metadata = ydl.extract_info(link, download=True)
    return metadata
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        Q_order = ""
        speak('song name')
        try:
            Q_order = r.recognize_google(audio, language='en-in')
        except Exception as e:
            speak("couldnt recognize,write the name pls")
            Q_order=input("song name=")
    return Q_order.lower()
song(get_audio())

#written by anshul raj(github-anshul3485raj) pls follow on github
