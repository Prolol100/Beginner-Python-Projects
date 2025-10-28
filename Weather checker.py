import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

user_input = input("Enter city name:")

resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

data = resp.json

try:
    weather = data()['weather'][0]['main' ]
    temp = round(((data()['main']['temp'])-32)*5/9)
except requests.HTTPError:
    print("API error:", resp.status_code, resp.text)
    exit()
except (KeyError, IndexError, ValueError):
    print("Unexpected API response format or invalid city.")
    exit()

print(f"The weather in {user_input} is: {weather}")
print(f"The temperature in {user_input} is: {temp}ºC")
