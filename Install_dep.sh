#!/bin/bash

sudo apt install portaudio19-dev
pip install pyttsx3 requests speechrecognition playsound wolframalpha gtts selenium pyAudio libespeak1 wikipedia google-cloud-storage numpy opencv-python pusher-push-notifications face_recognition
pip install -r requirements_drowsiness.txt requirements_face.txt
python setup.py

