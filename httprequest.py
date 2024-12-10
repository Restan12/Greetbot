import requests
import json
import random

def weather(api_key):
# URL of the API
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q=auto:ip&aqi=no"

    # Perform the GET request
    response = requests.get(url)
        #open the speech folder containing remarks on weather
    with open('Greetbot/speech/weather.json','r') as file:
        jsonData = json.load(file)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        location = f'{data['location']['name']},{data['location']['region']} {data['location']['country']}'
        # parsing the condition
        weatherToday= data['current']['condition']['text']

        remarks=random.choice(jsonData['weather'][weatherToday]['prompts'])
        data = f"Right now, On {location} is currently experiencing {weatherToday}. {remarks}"
       
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
