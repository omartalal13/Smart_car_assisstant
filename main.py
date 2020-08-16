#!/bin/bash

from subprocess import call
import multiprocessing
import os                                                               

# This block of code enables us to call the script from command line.                                                                                
def execute(process):                                                             
    os.system(f'{process}')   

# Creating the tuple of all the processes
all_processes = ('python openpose.py','python Gesture_Chatbot_Interaction.py','python drowsiness_detect.py','python ChatBot_Internal_wiki_search.py','python voice_commands.py')                                     
                                                                                     
                                                                                
rc = call("./facebash.sh", shell=True)
f = open("Driver_Name.txt", "r")
if (f !="unknown_person"):
    process_pool = multiprocessing.Pool(processes = 5)                                                        
    process_pool.map(execute, all_processes)
