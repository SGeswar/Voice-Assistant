import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
import smtplib
import json
from difflib import get_close_matches as gc




engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


#function for speech
def speak(audio):
          engine.say(audio)
          engine.runAndWait()
#function for greetings
def greeting():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")
    elif hour>=12 and hour<16:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    

    speak("This is IRIS Your voice Assistant. How may i help you")
#function for taking commands
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio = r.listen(source )

    try:
        print("recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please..")
        return "None"
    return query

#function for dictonary
data=json.load(open("/Users/gnan/Gnan/Coding/python/Assistant/data.json"))
def translate(w):
        w=w.lower()
        if w in data:
                return data[w]
        elif w.title() in data: 
                return data[w.title()]
        elif w.upper() in data: 
                return data[w.upper()]
        elif len(gc(w,data.keys()))>0:
                print("Did you mean %s" %gc(w,data.keys())[0])
                YN=input("if yes enter Y or else N")
                if YN=="Y":
                        return data[gc(w,data.keys())[0]]
                elif YN=="N":
                        return "Improper entry"

        else:
                return"Word dosent exist"


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('gnaneswarsub@gmail.com', 'typeritergm')
    server.sendmail('srigeswar@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
          greeting()
          while True:
              query=takeCommand().lower()
#con for wiki              
              if 'who' in query:
                  query=query.replace("wikipedia","")
                  results = wikipedia.summary(query, sentences=2)
                  speak("According to my source")
                  speak(results)

              elif 'what' in query:
                  query=query.replace("wikipedia","")
                  results = wikipedia.summary(query, sentences=2)
                  speak("According to my source")
                  speak(results)
#con for greeting             
              elif 'how are you' in query:
                  speak("i am fine sir . and i hope you are fine too...")

#con for intro
              elif 'about you' in query:
                  speak("I am IRIS. I was a piece of code in python written by GNAN ESWAR on 5 august 2019 as a personl assistant. To know what i can do just say how can you help me iris")
                  print(query)

#con for intro
              elif 'how can you help me iris' in query:
                  print("i can do few things for now....say who or what for knowing about a place or a person, say open youtube to open youtube, say open google for opening google, say search google or google search for searching something in google, say open dictionary to open english dictionary, say play music to play music, say send email to send email, say time now to know time and finally say exit to get rid of me")
                  speak("i can do few things for now....say who or what for knowing about a place or a person, say open youtube to open youtube, say open google for opening google, say search google or google search for searching something in google, say open dictionary to open english dictionary, say play music to play music, say send email to send email, say time now to know time and finally say exit to get rid of me hehehehehehhe")
                  
                  print(query)

#con for youtube
              elif 'open youtube' in query:
                    browser = webdriver.Chrome() 
                    browser.get('http://youtube.com/')
#con for google           
              elif 'open google' in query:
                 browser = webdriver.Chrome()
                 browser.get('http://google.com/')

              elif 'search google' in query:
                   speak("would u like to text or pronounce")
                   gourl="http://google.com/?#q=" 
                   query1=takeCommand().lower()
                   if 'text' in query1:
                       term=input("google search for..")
                       webbrowser.open(gourl+term)
                   elif 'pronounce' in query1:
                       speak("what should i search for boss") 
                       query2=takeCommand().lower()
                       webbrowser.open(gourl+query2)

#con for dict
              elif 'open dictionary' in query:
                       speak("would u like to text or pronounce")
                       query3=takeCommand().lower()
                       if 'pronounce' in query3:
                           speak("what word would you like to search for")
                           query4=takeCommand().lower()
                           meaning=translate(query4)
                           if type(meaning)==list:
                               for item in meaning:
                                   speak(item)
                                   print(item)
                           else:
                               print(meaning)
                               speak(meaning)
                       elif 'text' in query3:
                               speak("what word would you like to search for")
                               query4=input("what word would you like to search for")
                               meaning=translate(query4)
                               if type(meaning)==list:
                                 for item in meaning:
                                     speak(item)
                                     print(item)
                               else:
                                 print(meaning)
                                 speak(meaning)

 #con for music               
              elif 'play music' in query:
                  music_dir = ''
                  songs = os.listdir(music_dir)
                  print(songs)
                  os.startfile(os.path.join(music_dir,songs[6]))
#con for time
              elif 'time now' in query:
                  strTime = datetime.datetime.now().strftime("%H:%M:%S:")
                  speak(f"Boss, the time is {strTime}")
#con for arduino
              elif 'open your source code' in query:
                  speak("I am sorry....I cannot show my source code to everyone.. it may effect my perfomance....So please prove that you had access to the code ")
                  query5=takeCommand().lower()
                  if 'you can show me' in query5:
                      speak("your access granted. please make sure that you know what you are doing")
                      codePath = ""
                      os.startfile(codePath)
                  else:
                      speak("sorry your access denied")
#con for gmail
              elif 'send gmail' in query:
                  try:
                      speak("to whom do u want to send sir")
                      to=input("text mail")
                      speak("what should i send boss")
                      content = takeCommand()
                      sendEmail(to,content)
                      speak("email has been sent")
                  except Exception as e:
                        print(e)
                        speak("sorry boss i was unable to send the email at this moment")
#exit cond
              elif 'your service' in query:
                  speak("You are welcome boss. Run me when you required me. have a nice day")
                  break
#exit cond
              elif 'exit' in query:
                  speak("See you soon boss. have a nice day")
                  break
#exit cond

              elif 'get lost' in query:
                  speak("sorry that i was unable to help u boss")
                  break
              else:
                  speak("Sorry idk")

