import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

myName = "Pally" # Virtual Assistant name 

engine = pyttsx3.init('sapi5') #Creates a speech engine just like a speaker machine
voices = engine.getProperty('voices') #Get the engine voices available?
engine.setProperty('voice', voices[1].id) #Chooses which voice to use, voices[0] → usually male, voices[1] → usually female

def speak(audio):
    
    engine.say(audio) #Here is the text I want you to say.
    engine.runAndWait() #This line actually makes sound, Speak everything in the queue and wait until done

def wishme():
    hour = datetime.datetime.now().hour
    
    if hour >= 0 and hour <= 12:
        greet = "Good Morning"
    elif hour > 12 and hour < 18:
        greet = "Good Afternoon"
    else:
        greet = "Good Evening"

    speak(f"{greet}. I am {myName}, How may I help you?")

def hearMe():
    r = sr.Recognizer() #Creates a speech recognizer object
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source) #Records your voice
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US') #Sends the audio to Google, Converts speech → text, Stores it in query
        print("You Said:", query)
    except Exception:
        print("Say that again, please!")
        return "None"
    
    return query #Sends the recognized text back to the caller

#---------The section serves as a power button to init the Virtual Assistant----------------
if __name__ == "__main__": #prevents code from running on import, rather serves as a program rather as a module
    wishme()
    while True:  
        query = hearMe().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2) #Fetch a summary of a topic from Wikipedia, give me only 2 sentences from the summary.
            speak('According to wikipedia')
            print(result)
            speak(result)
        elif 'open google' in query:
            webbrowser.open('www.google.com')
        elif 'open instagram' in query:
            webbrowser.open('www.instagram.com')
        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
        elif 'play video' in query:
            video_dir = "C:\\Users\\ST FRANKLIN PC\\Documents\\Season 4"
            videos = os.listdir(video_dir)
            speak("Playing Video")
            video = os.path.join(video_dir, videos[3])
            os.startfile(video)
        else:
            search = 'www.google.com/search?q=' + query
            webbrowser.open(search)
