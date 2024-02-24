import requests
import datetime

while True:
    API_KEY = "3af6a928cddb412aeb910ed4c8ad4d57"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    print()
    city = input("City: ").title().strip()

    # api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=3af6a928cddb412aeb910ed4c8ad4d57

    requests_url = f"{BASE_URL}?q={city}&APPID=3af6a928cddb412aeb910ed4c8ad4d57"
    response = requests.get(requests_url)

    if response.status_code == 200:
        data = response.json()

        # print(data)

        country = data["sys"]["country"]
        print("Country: ", country)
        print()

        weather = data["weather"][0]["description"]
        print("Weather:     ", weather)

        temperature = data["main"]["temp"] - 273
        print("temperature: ", int(temperature), "°C")

        feelslike = data["main"]["feels_like"] - 273
        print("feels like:  ", int(feelslike), "°C")

        humidity = data["main"]["humidity"]
        print("Humidity:    ", humidity)

        windspeed = data["wind"]["speed"]
        print("Wind speed:  ", windspeed)

        print()
        dt = data["dt"]
        datetime_object = datetime.datetime.fromtimestamp(dt)
        print("Last updated:", datetime_object)

    else:
        print("An error occurred")

    print()
    print("Source: ", requests_url)
    print()
