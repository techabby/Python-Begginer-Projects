import requests


def weather(location):
    # API Key for OpenWeatherMap
    API_KEY = "cdca22a737d53204996d2bdd31f4ac73"

    # Use the correct API endpoint and pass the API_KEY as a query parameter
    weather_url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
    )

    weather_data = requests.get(weather_url).json()

    # Extract the relevant data from the API response
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    humidity = weather_data["main"]["humidity"]
    pressure = weather_data["main"]["pressure"]
    wind_speed = weather_data["wind"]["speed"]

    # Print the weather information
    print(f"Temperature: {temperature}")
    print(f"Description: {description}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Wind Speed: {wind_speed}")


# Input from the user
location = input("Enter the location: ")
weather(location)
