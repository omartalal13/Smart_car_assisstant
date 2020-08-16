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
 	 	audio = rObject.listen(source, phrase_time_limit = 3) 
 	print("Stop.") # limit 5 secs 

 	try: 
 		tic = time.time()
 		text = rObject.recognize_google(audio, language ='en-US') 
 		print("Time is", time.time() - tic)
 		print("You said: ", text) 
 		#speak(text) 
 		return text 

 	except: 

 		#speak("Could not understand your audio, PLease try again !") 
 		return 0			


WAKE = "voice"
SLEEP = "mute"
flag = False
print("Start")

while True:
    print("Listening")
    text = get_wake_audio()
    if text == WAKE:
        flag = True
        while(flag == True):
            
            f = open("Angle.txt", "r")
            Angle = float(f.readline())
            if(Angle >= 20 and Angle <= 40):
                print("Radio")

                text = get_audio()
                if text != 0:
                    if(text == "on"):
                        print("on")	
                    if(text == "off"):
                        print("off")
                    if(text == "forward"):
                        print("forward")
                    if(text == "backward"):
                        print("backward")	
                    if "go" in text :
                        print("go")
                        words = text.split()
                        print(words[1])	
            
            elif(Angle > 40 and Angle <= 65):
                print("AC")
                
                text = get_audio()
                if text != 0:                
                    if(text == "on"):
                        print("on")	
                    if(text == "off"):
                        print("off")
                    if(text == "increase"):
                        print("increase")
                    if(text == "decrease"):
                        print("decrease")	
                    if "set" in text :
                        print("set")
                        words = text.split()
                        print(words[1])	

            elif(Angle >= 70 and Angle <= 90):
                print("Right Window")
                
                text = get_audio()
                if text != 0:
                    if(text == "open"):
                        print("open")	
                    if(text == "close"):
                        print("close")  

            elif(Angle <= -70 and Angle >= -90):
                print("Left Window")
                
                text = get_audio()
                if text != 0:                
                    if(text == "open"):
                        print("open")	
                    if(text == "close"):
                        print("close")                                        
            text= get_audio()
            if text != 0:            
                if text == SLEEP:
                    speak("Ok BYe...")
                    flag = False	
	
