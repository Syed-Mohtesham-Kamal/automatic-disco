from Fuctions.online import play_on_youtube,search_on_google,send_whatsapp_message,send_email,search_on_wikipedia,get_random_joke,get_random_advice
import pyttsx3
import speech_recognition as sr
import datetime
from random import choice
from utils import opening_text
from pprint import pprint
import os

print("Initializing Marvel")
MASTER = "Kamal"

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour >= 0 and hour < 12:
        speak("Heyyyy,good morning" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("Heyyyy,good afternoon" + MASTER)

    else:
        speak("Heyyyy,good Evening" + MASTER)

    speak("i am Marvel. How may I help you?")



def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak(
            'Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


def main():
    speak("Initializing Marvel...")
    wishMe()
    query = takeCommand()

    if 'search on Wikipedia' in query:
        speak('What do you want to search on Wikipedia, sir?')
        search_query = takeCommand().lower()
        results = search_on_wikipedia(search_query)
        speak(f"According to Wikipedia, {results}")
        speak("For your convenience, I am printing it on the screen sir.")
        print(results)

    elif 'open command prompt' in query or 'open cmd' in query:
        open_cmd()

    elif 'open camera' in query:
        open_camera()

    elif 'open calculator' in query:
        open_calculator()

    elif 'video on YouTube' in query:
        speak("what do you want to play on Youtube, Sir?")
        video = takeCommand().lower()
        play_on_youtube(video)

    elif 'search on Google' in query:
        speak('What do you want to search on Google, sir?')
        query = takeCommand().lower()
        search_on_google(query)

    elif "send WhatsApp message" in query:
        speak(
            'On what number should I send the message sir? Please enter in the console: '
        )
        number = input("Enter the number: ")
        speak("What is the message sir?")
        message = takeCommand().lower()
        send_whatsapp_message(number, message)
        speak("I've sent the message sir.")

    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\dell\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[1]))

    elif 'what is the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif "send an email" in query:
        speak(
            "On what email address do I send sir? Please enter in the console: "
        )
        receiver_address = input("Enter email address: ")
        speak("What should be the subject sir?")
        subject = takeCommand().capitalize()
        speak("What is the message sir?")
        message = takeCommand().capitalize()
        if send_email(receiver_address, subject, message):
            speak("I've sent the email sir.")
        else:
            speak(
                "Something went wrong while I was sending the mail. Please check the error logs sir."
            )

    elif 'joke' in query:
        speak(f"Hope you like this one sir")
        joke = get_random_joke()
        speak(joke)
        speak("For your convenience, I am printing it on the screen sir.")
        pprint(joke)

    elif "advice" in query:
        speak(f"Here's an advice for you, sir")
        advice = get_random_advice()
        speak(advice)
        speak("For your convenience, I am printing it on the screen sir.")
        pprint(advice)


main()
