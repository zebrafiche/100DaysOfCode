# 310 Day 35 Goals_ what you will make by the end of the day

# Today we will learn about
# API Keys
# Authntication
# Environment Variables
# Sending SMS using python

# By the end of the day, we will have built a rain alert application


# 311 What is API Authentication and Why Do We Need to Authenticate Ourselves_

# Up until now we have only worked with free APIs
# Now it is time we worked with paid APIs
# Paid APIs have a free tier, we are going to work with that
# Now how do these API providers make sure that I do not abuse their free tier privileges?
# By authentication, meaning I will have an ID and a password
# And they will track how much I have used their API (there is a limit to how much you can use every month)


# 312 Using API Keys to Authenticate and Get the Weather from OpenWeatherMap

# Whenever we are using a new API, the most important thing is to read the documentation
# go to openweathermap.org
# sign up using your credentials
# get the API key
# if you want, you can generate a key specifically for a purpose, i have generated one, naming it python
API key = '03bc79f1ba83efcd61cb840fb0b1e344'


# There are a number of API services in the website -

# Current Weather Data
# Hourly Forecast 4 days
# Daily Forecast 16 days
# Climatic Forecast 30 days
# Global Weather Alerts Push notifications
# and many more...

# first, make a call to the API through the browser
# let's go to the Current Weather Data
# in the section "How to make an API call" find the API endpoint with parameters
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# the API endpoint ends with the question mark, everything after that are the parameters
# as you can see, it requires your latitude, longitude and API key
# when you paste this API endpoint in the browser, replace the parameters with the corresponding values

# and there you go, the weather details show up

# Challenge

# Go to the one call API and make an API call on pycharm
# At the time of writing this, one call API has become a premium service

# Let's move on with the current weather data API

import requests

api_key = '03bc79f1ba83efcd61cb840fb0b1e344'
MY_LAT = 23.810331
MY_LONG = 90.412521

parameters = {
    "appid": api_key,
    "lat": MY_LAT,
    "lon": MY_LONG

}

response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters)
response.raise_for_status()
# print(response)
# <Response [200]>
data = response.json()
# print(data)
# {
#     'coord': {'lon': 90.4125, 'lat': 23.8103},
#     'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}],
#     'base': 'stations',
#     'main': {'temp': 300.14, 'feels_like': 303.15, 'temp_min': 300.14, 'temp_max': 300.14, 'pressure': 1000, 'humidity': 83},
#     'visibility': 3500,
#     'wind': {'speed': 0, 'deg': 0},
#     'clouds': {'all': 75},
#     'dt': 1686442897,
#     'sys': {'type': 1, 'id': 9145, 'country': 'BD', 'sunrise': 1686438640, 'sunset': 1686487516},
#     'timezone': 21600,
#     'id': 1188909,
#     'name': 'Sāmāir',
#     'cod': 200
# }

# print(type(data))
# <class 'dict'>

for i in data['main']:
    print(f"{i}: {data['main'][i]}")
# temp: 300.14
# feels_like: 303.15
# temp_min: 300.14
# temp_max: 300.14
# pressure: 1000
# humidity: 83


# 313 Challenge - Check if it Will Rain in the Next 12 Hours

# The script needs to run every morning at 7 AM
# Check the weather
# Send a text message (or email) if it is going to rain today

# For now, try to extract the relevant data from the json output the API generates and print "Bring an Umbrella"

import requests

api_key = '03bc79f1ba83efcd61cb840fb0b1e344'
MY_LAT = 23.810331
MY_LONG = 90.412521

parameters = {
    "appid": api_key,
    "lat": MY_LAT,
    "lon": MY_LONG,
    "units": "metric",
    "cnt": 8
    # 'cnt' sets a limit to the timestamps that gets generated, details in the API doc
}

# Using the 5 day / 3 hour forecast API
response = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
data = response.json()

for i in data['list']:
    # when you view the API in browser, prettyprint the output, so you know the layout, and get what you want, like so
    print(f"{i['dt_txt']}: {i['weather'][0]['main']}, {i['weather'][0]['description']}")
for j in data['list']:
    if j['weather'][0]['main'] == 'Rain':
        print('Bring Umbrella')
        break


# 314 Sending SMS via the Twilio API

# The lesson uses a service called Twilio
# Sign up

# Timestamp - 02:48

# for the sake of practice I have tried to incorporate OOP here, making Twilio have its own class
# in the twilio_app.py file -
from twilio.rest import Client


class twilio:
    def __init__(self):
        self.account_sid = "AC11d33501f25cae1f5eea614843172b76"
        self.auth_token = os.environ["ad15cc22fef5353bbce8d38a6c99698d"]

    def send_text(self, message):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=message,
            from_="+13613154628",
            to="+8801681407930"
        )
        print(message.status)

# Additionally I want to make sure I get an email too, so another module named send_mail
# In the send_mail.py file -
import smtplib

my_email = 'rough.rafi@gmail.com'
my_password = 'fotkabazz1123581321'
app_password = 'uzdalqmxwenwmvmy'


class sm:
    def __init__(self):
        self.connection = smtplib.SMTP('smtp.gmail.com')

    def send_a_mail(self, message):
        self.connection.starttls()
        self.connection.login(user=my_email, password=app_password)
        self.connection.sendmail(from_addr=my_email,
                                to_addrs="rafi.abdullah.112358@gmail.com",
                                msg=f"Subject: Weather Update"
                                    f"\n\nHave a look at today's weather forecasts"
                                    f"\n\n{message}"
                                    f"\n\nHave a great day!"
                                    f"\n\nRegards."
                                    f"\nRafi")


# However, in the actual rain_alert.py file I haven't used twilio OOP but used the send_mail module
# in the rain_alert.py file -
import requests
from date_time import dt
from send_mail import sm
from twilio.rest import Client
import os

# to check where in the world it is actually raining, use - ventusky.com
# to get the coordinates of that place, use latlong.net

# IT IS RAINING CATS AND DOGS IN KAGOSHIMA RIGHT NOW, UPDATE LAT AND LONG TO KAGOSHIMA'S

api_key = '03bc79f1ba83efcd61cb840fb0b1e344'
MY_LAT = 31.596554
MY_LONG = 130.557114

# Twilio
account_sid = "AC11d33501f25cae1f5eea614843172b76"
# auth_token = os.environ["ad15cc22fef5353bbce8d38a6c99698d"]
auth_token = "ad15cc22fef5353bbce8d38a6c99698d"

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

if today.hour == 20:
    connect.send_a_mail(message)


# 315 Use PythonAnywhere to Automate the Python Script

# go to pythonanywhere.com
# sign in
# go to files
# upload your file, main.py or in this case, rain_alert.py
# open the file, click create bash console(at the bottom)
# in the console, type python3 rain_alert.py
# you can see that the code runs and it sends you a text

# In the video, Angela faced some problems getting the Twilio app to work in a hosting platform like pythonanywhere
# There were solutions posted in the pythonanywhere website
# She followed the solution and modified her code a little to get it to run
# Specifically, she changed 3 lines of code

# However, I did not face any such problem, maybe pythonanywhere changed their services to support twilio

# Schedule so that the code runs everyday
# go to tasks in pythonanywhere
# create a new task - daily, 07 AM (convert BD time to UTC) and command(python3 rain_alert.py)


# 316 Understanding Environment Variables and Hiding API Keys

# go to terminal and type gci env:

# Why do we need environment variables?
# 1. For convenience
# For example I have a large project that I deployed
# Occassionaly situations might require me to tweak some aspects
# But I do not want to change my main.py file, because it is so sensitive
# What I can do is, I can change the environment variables

# 2. For security
# You have uploaded you rain_alert.py file to pythonanywhere, a public server
# You realize that file contains your api_key, auth_token and account account_sid
# The api_key and the auth_token are more sensitive, since it can be traced back to the payment details
# So if this were a paid account, you'd be in trouble

# How to set environment variables?
# go to the terminal in pythoneverywhere, type -
# export variable_name=____________________
# for example, to set the API key as environment variable -
# api_key = '03bc79f1ba83efcd61cb840fb0b1e344'
# export twilio_api=03bc79f1ba83efcd61cb840fb0b1e344 (no spaces)

import os

# remove variable declaration from the editor, basically remove api_key = '03bc79f1ba83efcd61cb840fb0b1e344'
# then declare like this
api_key = os.environ.get(twilio_api)


# In pycharm -
# topright, click the rain_alert dropdown > edit configurations > click the button beside "environment variables"
# then use "+" to add your own
# use in the same way in code -
import os
api_key = os.environ.get("TWILIO_API_KEY")

# Angela showed everything in the context of pythonanywhere, which for some reason was not working at the time

# Now that you know how to work with APIs
# apilist.fun - you can find lots of cool APIs in here

