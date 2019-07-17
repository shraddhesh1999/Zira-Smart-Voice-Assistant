import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
from translate import Translator
import re
import requests








































engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

f=1

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am zira friend of shraddhesh How can i Help you?")

    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Zira is listening")
        #speak("Zira is listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("THINKing.....")
        query = r.recognize_google(audio, language='en-in')
        #print("you said:", query)
    except Exception as e:
        print(e)
        print("Say that Again.")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shraddheshshelkande99@gmail.com', '***************')
    server.sendmail('shraddheshshelkande99@gmail.com', to, content)
    server.close()    

if __name__ == "__main__":
    wishMe()
    while f==1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searchin in wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("Acoording to wikipedia")
            print(results)
            speak(results)

        elif 'hello zira' in query:
            speak("hello ")
        elif 'how are you' in query:
            speak("I am Fine How you doing?")
            print("Zira said: I am Fine")
        elif 'how doing' in query:
            speak("Better than last time!")
        elif 'which is the best' in query:
            speak("Previously there were few like alexa and siri but then,shraddhesh invented me")
        elif 'you are funny' in query:
            speak("yeah we do have some common traits")
        elif 'get tired' in query:
            speak("no i never get tired but your computer does!")
        elif 'joke' in query:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
            if res.status_code == requests.codes.ok:
                speak(str(res.json()['joke']))
                print(str(res.json()['joke']))
            else:
                speak('oops!I ran out of jokes')
        elif 'are you intelligent' in query:
            speak("beyound your imagination!!")
        elif 'can you rap' in query:
            speak("yo man i can drop beat")
            music_d = 'C:\\Users\\shrad\\Music\\Playlists\\new'
            songs = os.listdir(music_d)
            os.startfile(os.path.join(music_d,songs[0]))


        elif 'day today' in query:
            dayname = datetime.datetime.today().strftime("%A")
            print(f"Happy {dayname} to You!!!")
            speak(f"today is {dayname}")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")
        elif 'month' in query:
            mydate = datetime.datetime.now()
            month = mydate.strftime("%B")
            print(month)
            speak(f"{month} is going on")
        elif 'date' in query:
            x = datetime.datetime.now()
            print(x)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open website' in query:
            reg_ex = re.search('open website (.+)', "")
            if reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.' + domain
                webbrowser.open(url)
                print('Done!')
    

        elif 'play music' in query:
            music_dir = 'C:\\Users\\shrad\\shraddhesh\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'visual studio code' in query:
            codePath = "C:\\Users\\shrad\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                #to = "shraddheshshelkande@gmail.com"
                to=takeCommand("email address:")
                sendEmail(to, content)
                speak("Email sent")
            except Exception as e:
                print(e)
                speak("sorry shraddhesh i am unable to send the email now")
            else:
                pass
            finally:
                pass

        elif 'translate' in query:
             en=""
             r=sr.Recognizer()
             with sr.Microphone() as source:
                 print("speak into mic.")
                 audio=r.listen(source)
             try:
                 print("English:" + r.recognize_google(audio))
                 en=en+r.recognize_google(audio)
                 
             except sr.UnknownValueError:
                 print("Audio not Understandable.")
             except sr.RequestError as e:
                 print("cannot obtain results; {0}".format(e))
             
             print("which language you want")
             speak("which language you want")
             lang=takeCommand()
             translator= Translator(to_lang=lang)
             translation = translator.translate(en)
             print(translation)
             speak(translation)

        elif 'stop' in query:
            f = False
            speak("ok by until next time")

        else:
            speak("speak loudly and clearly!!!")


         
        


