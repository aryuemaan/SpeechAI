import pyttsx3
import speak as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir!")
    elif hour>=12 and hour<18:
        speak("good afternoon sir!")
    else:
        speak("good evening sir!")
    speak("i am Volva and i'm ready to take command")

def takecommand():
    #it takes microphones input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("recognizing.....")
        query = r.recognize_google(audio, language = 'en-in')
        print("user said:", query)
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query

if os.name == "main":
    WishMe()
    while True:
        takecommand()
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")#Add your Weblink or file location path inside the bracket#
        elif  'open gogoanime' in query:
            webbrowser.open('gogoanime.ai')#Add your Weblink or file location path inside the bracket#
        elif  'open canara bank' in query:
            webbrowser.open('') #####Add your Weblink or file location path inside the bracket#
        elif  'open google' in query:
            webbrowser.open("google.com")
        elif 'play hard music' in query:
            music_dir='D:\Photos Videos Music\Music Files'#Add your Weblink or file location path inside the bracket#
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif  'play soft music' in query:
            music_dir = 'D:\Photos Videos Music\Music Files'#Add your Weblink or file location path inside the bracket#
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")