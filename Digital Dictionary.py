from selenium import webdriver
import time
import os
import speech_recognition as sr
from gtts import gTTS
import playsound
import pyaudio
import random
import json
'''text to speech
Given input as text'''

def speak(bolo):
    x=str(random.randint(1,1100000))
    tts= gTTS(text= bolo , lang="en") #lang='hi'for hindi #convert the "text " file in to the audio file of language "en"(english).
    filename= "voice"+x+".mp3"                # Give a name to this file(audio file that is going to covert ).
    tts.save(filename)                   # Save this audiofile in your memory
    playsound.playsound(filename)       #play the coverted text
    os.remove(filename)
       


#will give input as voice
def audio():
    r= sr.Recognizer()              # device is ready to recognize (ears laga diye hai) ab bolne ke liye v kuch chaiye
    print("speak now")                   #bolne ka order de diye
    with sr.Microphone() as source:   # microphone me hi bolega so activated
        voice_input= r.listen(source)  #voice aa rha hai....usko sun rhaa hai computer
        said =""

        try:
            said= r.recognize_google(voice_input)       #google ka help le kr recognize v kr liya kya bole hai aur said me save kr diya
            print(said)
        except Exception as e:
            print("Exception: " +str(e))
            print("try again")
        return (said.lower())

def meaning(word):
    if word in data:
        speak("Your word is :" + word)
        print("Your word is :" + word)
        print(data[word])
        bolo=data[word]
        speak("Meaning of the word is " +bolo[0])
    elif word == "":
        speak( "Word is not present")
        speak("Try Again")
    else :
        speak( "Word is not present.Say update to update by yourself. or. say search to search in browser")
        ans=audio()
        if ans=="update":
            speak("Enter the meaning")
            updated_meaning=input("Enter the meaning of "+word+" :")
            new_data={word:[updated_meaning]}
            data.update(new_data)
            with open("source.json","w") as dictionary:
                json.dump(data,dictionary, indent=1)
                print("done")
                dictionary.close
        elif ans=="search":
            driver=webdriver.Chrome("C:\\Users\\raj ranjan\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
            driver.get('https://www.google.com/')
            driver.maximize_window()
            driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys("meaning of "+ word+" ")
            driver.find_element_by_xpath('//*[@id="tsf"]/div[2]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
            updated_meaning=input("Enter the meaning of "+word+" :")
            new_data={word:[updated_meaning]}
            data.update(new_data)
            with open("source.json","w") as dictionary:
                json.dump(data,dictionary, indent=1)
                print("done")
                dictionary.close  
        else :
            speak("ok")
            
with open("source.json") as dictionary:  
    data=json.load(dictionary)
    dictionary.close        
speak("Welcome to Digital Dictionary sir.")
print("      _______Welcome________\n")
speak("Speak your word sir ")
word = audio()
print("")
meaning(word)
while(True):
    speak("Do you want to search again. Say yes to continue or stop to end")
    command=audio()
    print("")
    if command =="yes":
        speak("Speak your word sir ")
        word = audio()
        print("")
        meaning(word) 
    if command=="stop":
        print("Thank you")
        break
            
speak("Thank you")









