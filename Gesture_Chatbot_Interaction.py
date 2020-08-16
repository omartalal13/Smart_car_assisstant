# Importing required libraries 
from googleplaces import types
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from gtts import gTTS                 # google text to speech 
from selenium import webdriver        # to control browser operations 
import time
import requests 
import json 
import speech_recognition as sr 
import playsound                      # to play saved mp3 file
import os                             # to save/open files 
import wolframalpha                   # to calculate strings into formula 
import pyttsx3
import numpy as np
import subprocess
import math

class GooglePlaces(object):
    def __init__(self, apiKey):
        super(GooglePlaces, self).__init__()
        self.apiKey = apiKey

    def search_places_by_coordinate(self, location, radius, types):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'location': location,
            'radius': radius,
            'types': types,
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(endpoint_url, params = params)
            results = json.loads(res.content)
            places.extend(results['results'])
            time.sleep(2)
        return places

    def get_place_details(self, place_id, fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        place_details =  json.loads(res.content)
        return place_details

def getLocation():
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver', chrome_options=options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()
    return (latitude,longitude)
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


WAKE = "wake up"
SLEEP = "sleep"
API_KEY = "AIzaSyA7lVwaqdd3odH9tzFgpQbeZG8wEJoBFeY"
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
            #text = "what is this building"		    
            if text == "what is this building":
                # Get Car cordinates 
                loc = getLocation()
                location = '{},{}'.format(loc[0], loc[1])
                #print(location)
                f = open("Angle.txt", "r")
                Angle = (float(f.readline())/ 180 ) * math.pi
                distance = 0.001
                kinect_Latitude  = float(loc[0]) + distance * math.cos(Angle)
                kinect_Longitude = float(loc[1]) + distance * math.sin(Angle)
                kinect_Magnitude = np.sqrt(np.add(np.power(kinect_Latitude,2),np.power(kinect_Longitude,2)))				
                Magnitude  = []		
                var_ID = []	
                api = GooglePlaces(API_KEY)				
                places = api.search_places_by_coordinate(location, "500", "restaurant")
                fields = ['name', 'formatted_address', 'international_phone_number', 'website', 'rating', 'review']
                for place in places:
                    Magnitude.append((np.sqrt(np.add(np.power(float(place['geometry']['location']['lat']), 2), np.power(float(place['geometry']['location']['lng']), 2)))) - kinect_Magnitude)
                    var_ID.append(place['place_id'])	

                Magnitude_desired  = min(filter(lambda x: x >= 0, Magnitude))	
                Magnitude_index    = Magnitude.index(Magnitude_desired)	
                Desired_ID = var_ID[Magnitude_index]
                #print (Magnitude)
                #print (kinect_Magnitude)				
                #print (Magnitude_desired)				
                #print (Magnitude_index)	
                #print (Desired_ID)
				
                fields = ['name', 'formatted_address', 'international_phone_number', 'website', 'rating', 'vicinity', 'opening_hours', 'price_level', 'review']						
                details = api.get_place_details(Desired_ID, fields)
								
                try:
                    website = details['result']['website']
                except KeyError:
                    website = ""
					 
                try:
                    name = details['result']['name']
                except KeyError:
                    name = ""
					 
                try:
                    address = details['result']['formatted_address']
                except KeyError:
                    address = ""
					 
                try:
                    phone_number = details['result']['international_phone_number']
                except KeyError:
                    phone_number = ""	
							
                try:
                    rating = details['result']['rating']
                except KeyError:
                    rating = ""		
							
                try:
                    vicinity = details['result']['vicinity']
                except KeyError:
                    vicinity = ""	
							
                try:
                    opening_hours = details['result']['opening_hours']
                except KeyError:
                    opening_hours = ""	
							
                try:
                    price_level = details['result']['price_level']
                except KeyError:
                    price_level = ""
							
                try:
                    reviews = details['result']['reviews']
                except KeyError:
                    reviews = []
									
                print("===================PLACE===================")
                print("Name:", name)	
                speak(name)				
                print("Website:", website)
                print("Address:", address)
                print("Phone Number:", phone_number)
                speak("phone_number is")				
                speak(phone_number)				
                print("Rating:", rating)
                speak("rating is")				
                speak(rating)				
                print("vicinity:", vicinity)
                print("price_level:", price_level)
                speak(price_level)				
                print("opening_hours:", opening_hours)			
                print("==================REWIEVS==================")
                for review in reviews:
                    author_name = review['author_name']
                    rating = review['rating']
                    text = review['text']
                    time = review['relative_time_description']
                    profile_photo = review['profile_photo_url']
                    print("Author Name:", author_name)
                    print("Rating:", rating)
                    print("Text:", text)
                    print("Time:", time)
                    print("Profile photo:", profile_photo)
                    print("-----------------------------------------")				
            #text = "goodbye assistant"				
            if text == SLEEP:
                speak("Ok BYe...")
                flag = False					
