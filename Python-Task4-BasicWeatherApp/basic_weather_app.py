import requests

def get_weather():
    print("Welcome to the Basic Weather App!")
    print("-" * 40)
    
    city = input("Enter the name of the city: ")
   
    api_key = "654cb00a494b26e5b3d96a5e538562de"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Check if city is found
        if data["cod"] == "404":
            print("Error: City not found. Please check the spelling.")
        elif data["cod"] == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_desc = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]
            
            print("\n--- Weather in {} ---".format(city.capitalize()))
            print(f"Temperature: {temp}°C")
            print(f"Condition:   {weather_desc.capitalize()}")
            print(f"Humidity:    {humidity}%")
            print(f"Wind Speed:  {wind_speed} m/s")
            print("-" * 40)
        else:
            print(f"Error: Unable to fetch data. Message: {data.get('message', 'Unknown error')}")
            
    except requests.exceptions.RequestException:
        print("Error: Network connection failed. Please check your internet.")

if __name__ == "__main__":
    get_weather()
