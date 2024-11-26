import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer=sr.Recognizer()
engine =pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', next((v.id for v in voices if "female" in v.name.lower()), voices[0].id))
newsapi = "1fd47a5fa8f6f32dcb629fb3695a4615"

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://gnews.io/api/v4/top-headlines?country=pk&category=general&apikey={newsapi}")
        r.raise_for_status()  # Raise an error for bad status codes
    
    # Parse the JSON response
        headlines = r.json()
        # Print the top headlines
        for i, article in enumerate(headlines.get("articles", []), 1):
            speak(f"{i}. {article.get('title')}")
        
    print(c)
if __name__== "__main__":
    speak("initializing robot")
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
       

        
        # recognize speech using Sphinx/google
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "robot"): 
                speak("Yes Sir")
                with sr.Microphone() as source:
                    print("Robot is activated")
                    #print("recogninzing your voice")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    speak(" ok sir")
                    processcommand(command)
            #print(command)
            #speak(command)
            
        except Exception as e:
            print("Error; {0}".format(e))

