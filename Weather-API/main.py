import requests
from twilio.rest import Client


ep = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "5ffe33122197306035a83c3a6cdcc19b"

account_sid = "AC490ecb5ca59efb6ae263bc6584bba4b0"
auth_token = "3f6427d3220843f87e9c9c3bf91baaec"
client = Client(account_sid, auth_token)


params = {
    "lat": 28.626989,
    "lon": 77.149643,
    "appid": api_key,
    "exclude": "current,daily,minutely"
}

response = requests.get(ep, params=params)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition = int(hour_data["weather"][0]["id"])
    print(condition)

    if condition < 700:
        will_rain = True

    else:
        will_rain = False

if will_rain:

    message = client.messages\
        .create(
        body="It will Rain today!",
        from_="+14697078801",
        to="+919871423702",
    )
if not will_rain:

    message = client.messages \
        .create(
        body="It will not Rain today!",
        from_="+14697078801",
        to="+919871423702",
    )



print(message.status)



