from gtts import gTTS 
import os , sys
import time
import wikipedia
import speech_recognition as sr
import playsound
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_wake_audio():
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=44100) as source:
    
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio , language ='en-US')
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

def get_audio(): 

 	rObject = sr.Recognizer() 
 	audio = '' 

 	with sr.Microphone() as source: 
 	 	print("Speak...") 
 		
 		# recording the audio using speech recognition 
 	 	audio = rObject.adjust_for_ambient_noise(source)
 	 	audio = rObject.listen(source, phrase_time_limit = 5) 
 	print("Stop.") # limit 5 secs 

 	try: 

 		text = rObject.recognize_google(audio, language ='en-US') 
 		print("You said: ", text) 
 		#speak(text) 
 		return text 

 	except: 

 		#speak("Could not understand your audio, PLease try again !") 
 		return 0			

def search_wiki(text):
    summary = wikipedia.summary(text, sentences = 1).encode('utf-8')
    return summary


WAKE = "start"
SLEEP = "end"
flag = False
print("Start")

while True:
    print("Listening")
    text = get_wake_audio()
    #text = "assistant"
    if text == WAKE:
        flag = True
        speak("Hi ,I am ready")
        while(flag == True):
            text = get_audio()
            if text != 0:		    
                if "what" in text or "search" in text:
                    text=text.split(' ',1)[1]
                    result = search_wiki(text)
                    speak(result)
                    print(result)
                if text == SLEEP:
                    speak("Ok BYe...")
                    flag = False	
	
