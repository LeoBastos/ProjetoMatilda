import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Bom Dia!")

    elif hour>=12 and hour<18:
        speak("Boa Tarde!")   

    else:
        speak("Boa Noite!")  

    speak("Olá, Eu Sou a Matilda. Como eu posso ajudar?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconhecimento...")    
        query = r.recognize_google(audio, language='pt-br')
        print(f"Você Disse: {query}\n")

    except Exception as e:
        # print(e)    
        print("Repita por favor...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@email', '339071leo')
    server.sendmail('email@email', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipédia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        

        elif 'horas' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"{strTime}")
        
        elif 'e-mail' in query:
            try:
                speak("O que você gostaria de dizer?")
                content = takeCommand()
                to = "email@email.com"    
                sendEmail(to, content)
                speak("Email Enviado!")
            except Exception as e:
                print(e)
                speak("Não Enviado")    
