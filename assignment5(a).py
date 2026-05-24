import requests

def weather_details(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=febbb9b919761422fe650a7c8f460605&units=metric"

    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()

        print("Temperature",data['main']['temp'])
        print("\nMin temperature",data['main']['temp_min'])
        print("\nTemperature feels_like",data['main']['feels_like'])
        print("\nHumidity",data['main']['humidity'])
        print("\nPressure",data['main']['pressure'])
        print("\nWind Speed:", data['wind']['speed'])
        print("\nWind Direction:", data['wind']['deg'],)
        print("\nVisibility:", data['visibility'])

    except requests.exceptions.RequestException as e:
        print(e)


city=input("Enter city name:")
weather_details(city)