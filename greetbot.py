
from datetime import datetime
import speech
import translate
import httprequest
from time import sleep

# Note: This bot use the https://www.weatherapi.com/ API
# Please register an account in the website and generate an api key

API_KEY='YOUR_API_KEY' #place the API KEY HERE
LANG='en' #language for speech and translation
# Note the LANG is use in translate


# determine the time today
time_now =datetime.now()
date=time_now.strftime("%D") #date
formatted_time = time_now.strftime("%H:%M %p") #time
hour = time_now.hour

# Determine the time of day
if 0 <= hour < 6:
    time_of_day = "Good Morning"
elif 6 <= hour < 12:
    time_of_day = "Good Morning"
elif hour == 12:
    time_of_day = "Good Noon"
elif 13 <= hour < 18:
    time_of_day = "Good Afternoon"
elif 18 <= hour < 21:
    time_of_day = "Good Evening"
else:
    time_of_day = "Good Night"

# Text to be converted to speech
text = f"{time_of_day}! Today is {date} and the time is {formatted_time}. " + httprequest.weather(API_KEY)
print(text)
# Uncomment if you want to translate it to your desired language
# text=translate.translate(text, LANG)
executed_times = set()
speech.speech(text, LANG)
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")  # Get the time in HH:MM format

    # Times to run TTS
    scheduled_times = ["08:00", "12:00", "18:00"]

    # Check if the current time matches any scheduled time and hasn't been executed yet
    if current_time in scheduled_times and current_time not in executed_times:
        # Run TTS
       speech.speech(text, LANG)

    # Sleep for a short period to avoid excessive CPU usage
    sleep(30)  # Check every 30 seconds