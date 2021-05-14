import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from datetime import date
import os
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<16:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("hello, how may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
        
    except Exception:
        print("sorry i couldn't get that can you please say that again")
        return "none"
    return query

def sendmail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("pc8722@gmail.com","8722431458p")
    server.sendmail("pc8722@gmail.com",to,content)
    server.close()

    
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if "summary" in query:
            speak("searching wikipedia....")
            query = query.replace('wikipedia'," ")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            speak('opening youtube')
            webbrowser.open("https://www.youtube.com/")

        elif "google" in query:
            speak('opening google')
            webbrowser.open('https://www.google.com/')

        elif "stack overflow" in query:
            speak('opening stackoverflow')
            webbrowser.open("https://www.stackoverflow.com/")

        elif "play some songs" in query:
            speak('playing music')
            webbrowser.open("https://music.youtube.com/")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif "date" in query:
            strfdate = datetime.datetime.today().strftime('%d/%m/%Y')
            print(f"sir, todays date is{strfdate}")
            speak(f"sir, todays date is{strfdate}")

        elif "instagarm" in query:
            speak('opening instagram')
            webbrowser.open("https://www.instagram.com/")

        elif "whatsapp" in query:
            speak('opening whatsapp')
            webbrowser.open('https://web.whatsapp.com/')
        
        elif "w3schools" in query:
            speak("opeing w3 schools")
            webbrowser.open("https://www.w3schools.com/")

        elif "classroom" in query:
            speak("opening google classroom")
            webbrowser.open("https://classroom.google.com/u/2/h")

        elif "amazon" in query:
            speak("opening amazon")
            webbrowser.open("https://amazon.in/")

        elif "flipkart" in query:
            speak("opening flipkart")
            webbrowser.open("https://flipkart.com/")

        elif "myntra" in query:
            speak("opening mynta")
            webbrowser.open("https://myntra.com/")

        elif "jio" in query:
            speak("opening ajio")
            webbrowser.open("https://ajio.com/")

        elif "watch movies" in query:
            speak("opening streamio")
            codepath1 = "C:\\Users\\desktop\\Desktop\\Stremio"
            os.startfile(codepath1)

        elif "my folder" in query:
            speak("opening your folder")
            codepath2 = "C:\\Users\\desktop\\Desktop\\Files\\pratham"
            os.startfile(codepath2)

        elif "my codes" in query:
            speak("opening your codes")
            codepath3 = "C:\\Users\\desktop\\Desktop\\Files\\pratham\\coding"
            os.startfile(codepath3)
        elif "email to" in query:
            try:
                speak("what should i send?")
                content = takecommand()
                to = takecommand()
                # sendmail(to,content)
                speak("sir the email has been sent!!")
            except Exception as e:
                print(e)
                speak("sorry, i couldn't send the email please try again")