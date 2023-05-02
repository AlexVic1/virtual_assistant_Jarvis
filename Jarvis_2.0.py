import pyttsx3 #pip install pyttsx3 == text dat into speach useing python
import datetime
import speech_recognition as sr #pip install SpeechRecognition == speech from mic to text
import smtplib
from secrets import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia 
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import string
import random
import psutil


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("Hello this is jarvis")
     
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("Hello this is Friday")    
    
    
    
def time ():
    Time = datetime.datetime.now().strftime("%I%M:%S") # hour = I, minutes = M, seconds = S
    speak("the current time is:")
    speak(Time)

def date(): 
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    #speak("The current date is:")
    #speak(date)
    #speak(month)
    #speak(year)
    
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("good morning sir!")
    elif hour >= 12 and hour <18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("Goof Night king!")                

def wishme():
    speak("hey Welcome back!")
    time()
    date()
    speak("jarvis at your service, please tell me how can i help you")
            
#while True:    
    #voice = int(input("Press for 1 for male voice\n Press2 for female voice\n"))
    #speak(voice)
    
#wishme()

def takeCommandCMD():  #"text" commend
    query = input("Please tell me how can i help you?\n")
    return query

def takeCommandMic():  #Mic Commend 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again... ")
        return "None"        
    return query

def sendEmail(receiver, subject, content):   #Send email 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email[subject] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendwhatsmsg(phone_no, message):   #Send What'sup Message
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+ '&text' +Message)
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():  #Google Search
    speak('what should is search for?')
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)

def news():     #NewsApi
    newsapi = NewsApiClient(api_key='89f14b78bfb541e9902c642d23022739')
    speak('what is the topic you would like')
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q='bitcoin',
                                     language='en',
                                     page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print((f'{x}{y["description"]}'))
        
    speak("that's it the update for today")              

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)
    
def screenshot():  #Screenshot take
    name_img = tt.time()
    name_img = f'C:\\Users\\ALEX\\Desktop\\python projects apps\\Audroino\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()  

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    
    passlen = 8
    s =[]
    s.extend(list(s1))
    s.extend(list(s2))     
    s.extend(list(s3))     
    s.extend(list(s4))
    
    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)
    
def flip():
    speak("okay, flipping a coin")
    coin = ['heads', 'tails']
    toss =[]
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    speak("i flipped the coin and got"+toss)

def roll():
    speak("okay, rolling a die for you")
    die = ['1', '2', '3', '4', '5', '6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak("i rolled a die and got"+roll)

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    
                       
if __name__ == "__main__":
    getvoices(2)
    wishme()
    while True:
        query = takeCommandMic().lower()     
        
        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()
        
        elif 'email' in query:
            email_list = {
                'test email':'pnftgqtzsotkpdzopv@bbitq.com'
            }
            try:
                speak("To who you want to send a email?")
                name = takeCommandMic()
                receiver = email_list[name]
                speak("what is the subject of the mail?")
                subject = takeCommandMic()
                speak('what should i say')
                content = takeCommandMic()
                sendEmail(receiver,subject, content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("unable to end the email")
        
        elif 'message' in query:
            user_name = {
                'Jarvis': ''# your phone number
            }
            try:
                speak("To who you want to send a whatsup?")
                name = takeCommandMic()
                phone_no = user_name[name]
                speak("what is the message?")
                message = takeCommandMic()
                sendwhatsmsg(phone_no, message)
                speak("message has been send")
            except Exception as e:
                print(e)
                speak("unable to send the message")                
        
        elif 'wikipedia' in query:
            speak('searching on wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)
        
        elif 'search' in query:
            searchgoogle()
            
        elif 'youtube' in query:
            speak("what should i search for you on Youtube")
            topic = takeCommandMic
            pywhatkit.playonyt(topic)
        
        elif 'weather' in query:
            city = 'tel aviv'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=182ad2d67cd06520b4813d2f1464f3c0'
            
            res = requests.get(url)
            data = res.json()
            
            weather = data['weather'] [0] ['main']
            temp = data['main']['temp']
            desp =data['weather'][0]['description']
            temp = round((temp - 32) * 5/9)
            print(weather)
            print(temp)
            print(desp)
            speak(f'weather in {city} is ')
            speak('Temperature : {} degree celcius'.format(temp))
            speak('weather is {} '.format(desp))
        
        elif 'news' in query:
            news()
        
        elif 'read' in query:
            text2speech()
            
        elif 'open' in query:
            os.system()
            
        elif 'open code' in query:
            codepath = 'C:\\Users\\ALEX\\Desktop\\python projects apps\\Audroino'
            os.startfile(codepath)
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'screenshot' in query:
            screenshot()    
        
        elif 'remember that' in query:
            data = takeCommandMic()
            speak("you said me to remember that:"+data)       
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close
        
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you told me to remember that "+remember.read())
            
        elif 'password' in query:
            passwordgen()
        
        elif 'flip' in query:
            flip()
        
        elif 'roll' in query:
            roll()
            
        elif 'cpu' in query:
            cpu()
                             
        elif 'offline' in query:
            quit()            
                           
                           
# takeCommandMic == "hey jarvis what is the day today" tokenize ['hey', 'jarvis', 'that', 'is', 'the', 'day', 'today']                           
                           