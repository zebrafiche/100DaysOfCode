# TODO 0 Import modules and declare variables
import requests
import json
import datetime as dt
import smtplib
import time

MY_LAT = 23.810331
MY_LONG = 90.412521
# These are Dhaka's latitudes and longitudes

my_email = 'rough.rafi@gmail.com'
my_password = 'fotkabazz1123581321'
app_password = 'uzdalqmxwenwmvmy'
message = 'Subject: Look Up!!!\n\nHello, ISS is passing overhead and it is nighttime. Look Up.\nRegards,\nRafi'


# TODO 1 - Get ISS location
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.raise_for_status())
data = response.json()
# print(data)
# {'timestamp': 1685485594, 'iss_position': {'latitude': '28.5937', 'longitude': '-16.3372'}, 'message': 'success'}
# print(data['iss_position'])
# {'latitude': '25.9490', 'longitude': '-153.3199'}
# print(data['iss_position']['longitude'])
# -153.3199
formatted_data = json.dumps(data, indent=1)
# print(formatted_data)
# {
#  "message": "success",
#  "iss_position": {
#   "latitude": "25.9490",
#   "longitude": "-153.3199"
#  }


# TODO 2 - Get sunrise and sunset time in Dhaka
# TODO 2a - Turn off the formatting for the times, so the formatting matches both datetime and api
# Second response to get the sunrise and sunset data in my city

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    'formatted': 0,
}

response2 = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response2.raise_for_status()

data2 = response2.json()

formatted_data2 = json.dumps(data2, indent=1)
# print(formatted_data2)
# {
#  "results": {
#   "sunrise": "2023-05-29T23:10:03+00:00",
#   "sunset": "2023-05-30T12:41:37+00:00",
#   "solar_noon": "2023-05-30T05:55:50+00:00",
#   "day_length": 48694,
#   "civil_twilight_begin": "2023-05-29T22:46:16+00:00",
#   "civil_twilight_end": "2023-05-30T13:05:24+00:00",
#   "nautical_twilight_begin": "2023-05-29T22:16:21+00:00",
#   "nautical_twilight_end": "2023-05-30T13:35:19+00:00",
#   "astronomical_twilight_begin": "2023-05-29T21:45:14+00:00",
#   "astronomical_twilight_end": "2023-05-30T14:06:26+00:00"
#  },
#  "status": "OK"
# }

dhaka_sunrise = data2['results']["sunrise"]
dhaka_sunset = data2['results']["sunset"]
# print(dhaka_sunrise)
# 2023-05-27T23:10:27+00:00
# print(dhaka_sunset)
# 2023-05-28T12:40:42+00:00


# TODO 3 - Get current time and date

now = dt.datetime.now()
# print(now)
# 2023-05-29 05:31:16.402111


# TODO 4 - Compare the two times
dhaka_sunrise = dhaka_sunrise.split('T')
dhaka_sunrise = dhaka_sunrise[1].split(':')[0]
dhaka_sunset = dhaka_sunset.split('T')
dhaka_sunset = dhaka_sunset[1].split(':')[0]

# print(dhaka_sunrise)
# 23
# print(dhaka_sunset)
# 12
hour = now.hour
# print(hour)
# 5


# TODO 6 - Compare your location with ISS location
# ISS does not have to be exactly at MY_LAT and MY_LONG, you can give a range here
def iss_in_range():
    upper_lat_limit = MY_LAT + 5
    lower_lat_limit = MY_LAT - 5
    upper_lng_limit = MY_LONG + 5
    lower_lng_limit = MY_LONG - 5
    if lower_lng_limit < data['iss_position']['longitude'] < upper_lng_limit:
        if lower_lat_limit < data['iss_position']['latitude'] < upper_lat_limit:
            return True


# TODO 7 - Check if nighttime
# print(type(dhaka_sunrise))
# <class 'str'>


def is_night_time():
    if int(dhaka_sunset) < now.hour < 24 and 0 < now.hour < int(dhaka_sunrise):
        return True


# TODO 8 - Send a mail if iss is overhead and it is nighttime
# TODO 8a - Make the code run continuously to check if ISS is overhead
while True:
    time.sleep(300)
    if iss_in_range() and is_night_time():
    # if now.hour == 5:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="rafi.abdullah.112358@gmail.com",
                                msg=message)
