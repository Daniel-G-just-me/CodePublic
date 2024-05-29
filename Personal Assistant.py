import speech_recognition as sr
import pyttsx3
import datetime
import requests
import time
import pywhatkit
import os
import wikipedia

engine = pyttsx3.init()
engine.setProperty("rate", 180)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    print("Listenting...")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 30)
    try:
        return r.recognize_google(audio)
    except Exception as e:
        print("Skipping unknown error.")
        main()

def cloths():
    api_key = "44f032dd893856f813884fa657344f8a"
    location = "Enfield Town, GB"
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    temp_kelvin = weather_data["main"]["feels_like"]
    temp_celsius = temp_kelvin - 273.15
    cloths = ""
    if temp_celsius < 6:
        cloths = "Wear a warm coat, hat, gloves, and a scarf, if your doing exercise wear a hoodie and trousers   "
    elif temp_celsius < 13:
        cloths = "Wear a jumper, jacket and trousers, if doing exercise wear a long sleave top and trousers   " 
    elif temp_celsius < 18:
        cloths = "Wear a jacket, long sleve t shirt and trousers, if doing exercise wear a short sleeve top and trousers   "
    elif temp_celsius < 21:
        cloths = "Wear a t-shirt and trousers and a hat if sunny, if doing exercise wear a t-shirt and shorts and a hat if sunny   "
    else:
        cloths = "Wear a t-shirt and shorts and a hat if sunny, dont do exercise its too hot   "
    rain = ""
    if "rain" in weather_data:
        rain = "  and bring an umbrella or rain coat, it's looking a bit drippy"
    else:
        rain = "  and no rain forecasted  "
    sentence = cloths + rain
    return sentence

def countdown(tick_tock):
    speak("Timer starting,")
    while tick_tock:
        mins, secs = divmod(tick_tock, 60)
        time.sleep(0.9999999999999999999999999)
        tick_tock -= 1
    speak("times up!")

def news():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'GB',  
        'apiKey': '9f353fd9d7d649548308e21b6a7d8c29'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        for article in articles:
            speak(article['title'])
            print(article['url'])
    else:
        speak('Failed to get news: ', response.text)

#speak(". . . all systems up! Hello my name is Bex, I am your personal A I assistant. I will be listening for any of your commands")

def main():
    while True:

        current_time = datetime.datetime.now().time()
        formatted_time = current_time.strftime('%H:%M:%S')
        print(formatted_time)

        command = listen()
        if command != "" and command is not None:
            print(command)
            if "what's your name" in command:
                speak("My name is Bex, I was made by Daniel")
            elif "how are you" in command:
                speak("I don't have eny emotion circuits, but if your into that sort of thing I'm ok.")
            elif "life the universe and everything" in command:
                speak("42.")
            elif "date" in command:
                strdate=datetime.datetime.now().strftime("%A:%d:%B(%m)%Y")
                speak(f"The date is {strdate}")
            elif "motivation" in command:
                speak("There is nothing impossible to they who will try.")
            elif "exit" in command:
                speak("Goodbye!")
                break
            elif "quit" in command:
                speak("Goodbye!")
                break
            elif "youtube" in command.lower():
                command =command.replace("youtube", "")
                pywhatkit.playonyt(command)
                speak("Done, enjoy.")
            elif "video" in command.lower():
                command =command.replace("video", "")
                pywhatkit.playonyt(command)
                speak("Done, enjoy.")
            elif "google" in command.lower():
                command =command.replace("Google", "")
                pywhatkit.search(command)
                speak("Done.")
            elif "search" in command.lower():
                command =command.replace("search", "")
                pywhatkit.search(command)
                speak("Done.")
            elif "countdown" in command.lower():
                speak("How long in seconds?")
                tick_tock = listen()
                print(tick_tock)
                countdown(int(tick_tock))
            elif "timer" in command.lower():
                speak("How long in seconds?")
                tick_tock = listen()
                print(tick_tock)
                countdown(int(tick_tock))
            elif "cloths" in command.lower():
                speak(cloths())
            elif "weather" in command.lower():
                speak(cloths())
            elif "wear" in command.lower():
                speak(cloths())
            elif "news" in command.lower():
                news()
                speak("Now your all caught up with whats happening.")
            elif "thanks" in command.lower():
                speak("No problem. If you where being sarcastic I can't tell l o l")
            elif "thank you" in command.lower():
                speak("No problem. If you where being sarcastic I can't tell l o l")
            elif 'explain' in command.lower():
                speak('Searching Wikipedia...')
                command =command.replace("explain", "")
                results = wikipedia.summary(command, sentences=3)
                speak(results)
            elif "time" in command:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")
            elif "morning" in command.lower():
                speak("Good morning Daniel")
                speak("Here are todays headlines")
                news()
                speak(cloths())
                dt = datetime.datetime.now()
                day = dt.strftime('%A')
                speak("today is " + day)
                speak("Have a good day.")
            else:
                print("Unknown command.")
    
        else:
            print("Nothing said.")

main()