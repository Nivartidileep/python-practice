'''
virtual Assistance ---> make conversion,locate maps,greetings...
'''
#TTS ---> gTTS

import gtts
from gtts import gTTS
#import playsound
#now we willgive a text and convert to audio
#text = "vizag is a city of destiny"
#g = gTTS(text)
#save as audio file (.mp3)
#g.save("audio.mp3")
#playsound.playsound('audio.mp3')

#SpeechRecognition (STT) --> pip install speechRecognition

import gtts
from gtts import  gTTS
import speech_recognition as sr
from time import ctime #it returns current time
import os
import playsound
import uuid
import webbrowser

#first we will make our virtualAssiatant to understand what we speak
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Now you can start talking")
        audio = r.listen(source,phrase_time_limit = 5)
        #what ever we speak lets store in data
    data = ""
    #now we will give our Exception handling here to avoid any errors
    try:
        data = r.recognize_google(audio,language="en-US")
        print("You said:",data)
    except sr.UnknownValueError as e:
        print("Make sure to speak louder,so it can be heard")
    except sr.RequestError as e:
        print("Request failed,please check your internet connection")
    return data
    #text = gTTS(data)
    #text.save('new.mp3')
    #playsound.playsound('new.mp3')
#listen()
    
#listen() #needs to have pyaudio --> pip install pyaudio

def respond(String):
    """Responding function to get audio saved and text is spoken back"""
    print(String)
    tts = gTTS(text=String)
    tts.save("Speech.mp3")
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

#we will use above

#next we will make our virtualassistant to work with given conditions

def va(data):
    """now we will map our condtions"""
    if "hello" in data:
        listening = True
        respond("hey hai good to see you")
    elif "how are you" in data:
        listening = True
        respond(ctime())
    elif "what your plans" in data:
        listening = True
        respond("Emi ledu chadvukoo baguntundi")
    elif "open Google" in data:
        listening = True
        url = "https://www.google.com"
        webbrowser.open(url)
        print("success")
        respond("Done opened")
    elif "locate" in data:
        listening = True
        url = "https://www.google.com/maps/search/"
        webbrowser.open(url+data.replace("locate",""))
        print("Located")
        respond("Done maps opened")
    elif "my favorate song" in data:
        listening = True
        url = "https://www.youtube.com"
        print("success")
        respond("Done")
    elif "stop talking" in data:
        listening = True
        respond("calm")
    try:
        return listening
    except UnboundLocalError:
        print("Mismatched speak correctly")
respond("hey dileep")
listening = True
while listening:
    data = listen()
    listening = va(data)
    
    
