import requests  # Weather data ko lene ke liye

# Apni OpenWeatherMap wali API key yahan paste karo:
api_key = "4db149efcd9003477b36631ccc787e65"

# User se city ka naam ya zip mangna
city = input("Enter city name or zip code: ")

# Weather API URL banana (city ke basis pe)
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Data mangwana (API call)
try:
    response = requests.get(url)
    data = response.json()
    if data.get("cod") == 200:   # 200 means city mil gayi
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']
        wind = data['wind']['speed']

        print(f"\nWeather in {city.title()}:")
        print(f"Condition: {condition.capitalize()}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%\n")
        print(f"Wind Speed: {wind} m/s")
        
    else:
        print("City name galat hai ya data nahi mila. Try again.")
except Exception as e:
    print("Kuch problem aa gayi! Internet ya API key check karo.")
