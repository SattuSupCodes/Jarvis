import pyttsx3 
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour <18:
        speak("Good afternoon")
    else:
        ("Good Evening")
    speak("I'm Jarvis. How may I assist you today?")
if __name__  == "__main__":
    # speak("sattu is a cutie")
    wishMe()
    
# my real mission is to make my terminal talk btw. This is just me getting severely distracted in the process