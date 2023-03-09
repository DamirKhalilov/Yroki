import requests

OPENWEATHERTOKEN ='dc09ede661b9bf605e28c882ea1fc240'
city = input('City name: ')

try:
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERTOKEN}&units=metric&lang=ru')
    data = response.json()

    city = data["name"]
    des = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    country = data["sys"]["country"]
    # sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M')
    # sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M')
    print(
        f"City: {city}\n"
        f"Current temp: {temp}\n"
        f"Weather: {des}\n"
        f"Humidity: {humidity}\n"
        f"Wind speed: {wind}\n"
        f"Country code: {country}\n"
        # f"Sunrise: {sunrise}\n"
        # f"Sunset: {sunset}\n"

    )
except Exception as ex:
    print(ex)



    # with open('file.txt','w') as f:
    #     f.write(str(data)