import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import time
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[1].id)
#rate = engine.getProperty('rate')
#print (rate)
engine.setProperty('rate', 175)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def WishOnStartup():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("Hello Rohit, Good Morning")
        speak("Hello Rohit, Good Morning")
    elif hour>=12 and hour<18:
        print("Hello Rohit, Good Afternoon")
        speak("Hello Rohit, Good Afternoon")
    else:
        print("Hello Rohit, Good Evening")
        speak("Hello Rohit, Good Evening")


def instructions():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening now...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"You asked: {statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


WishOnStartup()


if __name__=='__main__':


    while True:
        speak("How can I help you")
        statement = instructions().lower()
        if statement==0:
            continue

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is opened")
            time.sleep(5)

        elif 'open youtube music' in statement or "play music" in statement:
            webbrowser.open_new_tab("https://music.youtube.com")
            speak("Youtube Music is opened")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is opened")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail is opened")
            time.sleep(5)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M")
            speak(f"the time is {strTime}")

        elif "open leetcode" in statement:
            webbrowser.open_new_tab("https://leetcode.com/problemset/all/")
            speak("Here is leetcode, Have a great time solving problems!")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://news.google.co.in/")
            speak('Here are some headlines from Google News. Happy reading')
            time.sleep(6)

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am your persoanl assistant. I perform minor tasks like opening youtube, google chrome, gmail and leetcode , predict time, search, get news headlines from The TOI')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Rohit")
            print("I was built by Rohit")


        elif "goodbye" in statement or "ok bye" in statement or "shut down" in statement:
            print('Assistant shutting down. Good bye')
            speak('Assistant shutting down. Good bye')
            break

time.sleep(3)

