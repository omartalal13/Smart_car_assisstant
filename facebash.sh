#!/bin/bash

str=unknown_person


for i in 1 2 3
do
	python webcam-capture.py; face_recognition ./Known/ ./Unknown/ | cut -d ',' -f2 > Driver_Name.txt
	if [[ $(< Driver_Name.txt) != "$str" ]]
	then
		break
	else
		if [[ $i == 3 ]]
		then 
			python Notification.py

		fi
	fi	
done
echo $(<Driver_Name.txt)
