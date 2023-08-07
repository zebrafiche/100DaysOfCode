import requests
from date_time import dt
from send_mail import sm
from twilio.rest import Client
import os

# to check where in the world it is actually raining, use - ventusky.com
# to get the coordinates of that place, use latlong.net

# IT IS RAINING CATS AND DOGS IN KAGOSHIMA RIGHT NOW, UPDATE LAT AND LONG TO KAGOSHIMA'S

api_key = os.environ.get("TWILIO_API_KEY")
MY_LAT = 31.596554
MY_LONG = 130.557114

# Twilio
account_sid = "AC11d33501f25cae1f5eea614843172b76"
# auth_token = os.environ["ad15cc22fef5353bbce8d38a6c99698d"]
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

parameters = {
    "appid": api_key,
    "lat": MY_LAT,
    "lon": MY_LONG,
    "units": "metric",
    "cnt": 8
}

# Using the 5 day / 3 hour forecast API
response = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
# print(response)
# <Response [200]>
data = response.json()
# print(data)
# {
#   "cod": "200",
#   "message": 0,
#   "cnt": 8,
#   "list": [
#     {
#       "dt": 1686528000,
#       "main": {
#         "temp": 26.99,
#         "feels_like": 30,
#         "temp_min": 26.41,
#         "temp_max": 26.99,
#         "pressure": 999,
#         "sea_level": 999,
#         "grnd_level": 999,
#         "humidity": 83,
#         "temp_kf": 0.58
#       },
#       "weather": [
#         {
#           "id": 500,
#           "main": "Rain",
#           "description": "light rain",
#           "icon": "10d"
#         }
#       ],
#       "clouds": {
#         "all": 75
#       },
#       "wind": {
#         "speed": 2.89,
#         "deg": 119,
#         "gust": 6.06
#       },
#       "visibility": 10000,
#       "pop": 0.28,
#       "rain": {
#         "3h": 0.13
#       },
#       "sys": {
#         "pod": "d"
#       },
#       "dt_txt": "2023-06-12 00:00:00"
#     },
#     {
#       "dt": 1686538800,

# print(type(data))
# <class 'dict'>
message = ""
for i in data['list']:
    # when you view the API in browser, prettyprint the output, so you know the layout, and get what you want, like so
    message += f"{i['dt_txt']}: {i['weather'][0]['main']}, {i['weather'][0]['description']}"
    message += '\n'
for j in data['list']:
    if j['weather'][0]['main'] == 'Rain':
        message += 'Bring Umbrella'
        # this part is exclusively for if you are using Twilio to send a text message as well
        # ignore till the loop break if you will not be using Twilio
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_="+13613154628",
            to="+8801681407930"
        )
        print(message.status)
        break
print(message)
# 2023-06-12 00:00:00: Rain, light rain
# 2023-06-12 03:00:00: Clouds, broken clouds
# 2023-06-12 06:00:00: Rain, moderate rain
# 2023-06-12 09:00:00: Rain, light rain
# 2023-06-12 12:00:00: Rain, light rain
# 2023-06-12 15:00:00: Rain, light rain
# 2023-06-12 18:00:00: Clouds, broken clouds
# 2023-06-12 21:00:00: Clouds, overcast clouds
# Bring Umbrella


today = dt()
connect = sm()

# if today.hour == 4:
#     connect.send_a_mail(message)
