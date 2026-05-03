import requests

api_key="105340f9fdcada19de3d0b7ee93c3c1c"
api_endpoint="https://api.openweathermap.org/data/2.5/forecast"

weather_param={
    "lat":28.704060,
    "lon":77.102493,     #delhi
    "appid":api_key,
    "cnt":4,
}

result=requests.get(api_endpoint,params=weather_param)
data=result.json()
for weather_data in data["list"]:
    condition=weather_data["weather"][0]["id"]

    if int(condition) < 700 :
        print("Bring Umbrella")
    else:
        print("Don't Bring Umbrella")
