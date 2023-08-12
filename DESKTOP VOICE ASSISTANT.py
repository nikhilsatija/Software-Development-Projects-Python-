import pyttsx3  # python text-to-speech library
import speech_recognition  # To take microphone input from the user

import wikipedia  # To do Wikipedia searches
import pywhatkit
import os  # To interact with the os
import random
import smtplib  # Simple Mail Transfer Protocol library - (SMTP) is a protocol that allows us to send emails and route emails between mail servers
import webbrowser  # To open any website in a web browser (built-in module)
from datetime import datetime, date


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wishme():
    speak("\nHi, I'm JARVIS. Tell me How may I help you?")


def take_command():
    # It takes voice input through microphone from the user and return string output

    global audio_input
    listener = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as microphone_input:
        print("\nListening...")
        listener.pause_threshold = 1
        audio = listener.listen(microphone_input)

    try:
        print('Recognising...')
        audio_input = listener.recognize_google(audio, language='en-in')
        print(f"\n{audio_input}\n")

    except Exception:
        speak("\nSorry I didn't get it. Say that again please\n")
        take_command()

    return audio_input
 

def send_email(to_whom, what_content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    with open('C:\\Users\\lenovo pc\\OneDrive\\OneNote\\pwd.txt', 'r') as file:
        read_pwd = file.read()

    server.login('johnkardon666@gmail.com', read_pwd)
    server.sendmail('johnkardon666@gmail.com', to_whom, what_content)
    server.close()


engine = pyttsx3.init('sapi5')  # Creating an object named 'engine' & 'sapi5' - Microsoft developed Speech API which provides voices to the Windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

if __name__ == '__main__':
    wishme()
    while True:
        query = take_command()
        query = query.lower()

        if 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)

        elif 'who are you' in query:
            wishme()

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com")

        elif 'youtube' in query:
            try:
                speak("Tell the keyword on which you want to play the video")
                topic = take_command()
                pywhatkit.playonyt(topic)
                print("Playing...")

            except Exception:
                speak("Sorry, Currently I'm not able to play the video")

        elif 'open whatsapp' in query:
            speak("Opening WhatsApp")
            webbrowser.open("https://web.whatsapp.com")

        elif 'whatsapp' in query:
            try:
                speak("Enter receiver's phone number with country code")
                ph_no = str(input())
                speak("\nSpeak, What message you want to send?")
                msg = take_command()
                pywhatkit.sendwhatmsg_instantly(phone_no=ph_no, message=msg)
                speak("Check and Press enter to send the same.")

            except Exception:
                speak("Sorry, I'm not able to send this message.")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'google' in query:
            try:
                speak("Tell what you want to search")
                search_topic = take_command()
                pywhatkit.search(search_topic)

            except Exception:
                speak("Sorry, Currently I'm not able to search it")

        elif 'visual studio' in query:
            speak("Opening Visual Studio Code")
            os.startfile("C:\\Users\\lenovo pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'pycharm' in query:
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2\\bin\\pycharm64.exe")

        elif 'notepad' in query:
            speak("Opening Notepad")
            os.startfile("C:\\Windows\\system32\\notepad.exe")

        elif 'browser' in query:
            speak("Opening Chrome")
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        elif 'song' in query:
            path = "F:\\Music\\SONGS\\Arijit singh songs"
            songs = os.listdir(path)
            random_song = random.randint(0, len(songs) - 1)
            speak(f"Playing song {songs[random_song].rstrip(songs[random_song][-4:])}")  # rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
            os.startfile(os.path.join(path, songs[random_song]))  # os.path.join() method in Python join one or more path components intelligently. This method concatenates various path components with exactly one directory separator (‘/’) following each non-empty part except the last path component
            exit()

        elif 'time' in query:
            t = datetime.now().strftime("%I:%H %p")
            speak(f"It's {t}")

        elif 'date' in query:
            day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            speak(f"It is {day_name[date.today().weekday()]}, {date.today().strftime('%dth of %B %Y')}")

        elif 'day' in query:
            day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            speak(f"Today is {day_name[date.today().weekday()]}")

        elif 'instagram' in query:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com/_nikhilsatija/", new=2)

        elif 'telegram' in query:
            speak("Opening Telegram")
            webbrowser.open("https://web.telegram.org/", new=2)

        elif 'facebook' in query:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com/", new=2)

        elif 'email' in query:
            try:
                speak("\nSpeak, What message you want to send?")
                content = take_command()
                speak("Enter receiver's email id")
                to = str(input())
                send_email(to, content)
                speak("You can Check! Email has been sent successfully.")

            except Exception:
                speak("Sorry, I'm not able to send this email.")

        elif 'exit' in query:
            speak("Okay! I'm exiting...")
            exit()

        else:
            speak("\nSorry, I can't help with what you said.")
            speak("Please refer to my Supported tasks list.")

            speak("\nWanna ask me something else? Say Yes or No")
            want_user_audio_input = take_command()

            if 'yes' in want_user_audio_input:
                speak("Say, What you want. I'm hearing...")

            elif 'no' in want_user_audio_input:
                speak("Okay then, I'm exiting...")
                exit()

            else:
                speak("Didn't recognise! But I'm still hearing. Just ask what you want")