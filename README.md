####libraries needed####

> sudo pip install pyttsx3
> sudo pip install requests
> sudo pip install --upgrade speechrecognition
> sudo pip install playsound
> sudo pip install wolframalpha
> sudo pip install gtts
> sudo pip install selenium
> sudo apt-get install portaudio19-dev
> sudo pip install PyAudio
> sudo apt install libespeak1
> sudo pip install wikipedia
> sudo pip install google-cloud-storage
> sudo pip install numpy
> sudo pip install -r requirements_drowsiness.txt
> sudo pip install opencv-python
> sudo pip install pusher-push-notifications
> sudo pip install -r requirements_face.txt
> sudo pip install face_recognition
> python setup.py install


####Install needed####

## Geckodriver
wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.23.0-linux64.tar.gz -O > /usr/bin/geckodriver'
sudo chmod +x geckodriver
rm geckodriver-v0.23.0-linux64.tar.gz

## Chromedriver
wget https://chromedriver.storage.googleapis.com/76.0.3809.68/chromedriver_linux64.zip
unzip /tmp/chromedriver_linux64.zip
mv chromedriver /usr/bin/chromedriver
chown root: /usr/bin/chromedriver
chmod 755 /usr/bin/chromedriver

### To Run ###
> python main.py


