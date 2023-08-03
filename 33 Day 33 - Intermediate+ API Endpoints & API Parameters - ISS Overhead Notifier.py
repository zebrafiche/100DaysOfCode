# 294 Day 33 Goals_ what you will make by the end of the day

# Today we will learn about application programming interface (API)
# By the end of the day, we will build an application to track the movement of ISS
# ISS - International Space Station


# 295 What are Application Programming Interfaces (APIs)_

# There are many websites that have a lot of data
# Yahoo Weather gives you weather stats
# Coinbase gives you crypto stats
# NBA website gives you stats on various crypto currencies

# What if we wanted to use the data that they have in our program?

# Application Programming Interface - API
# APIs are set of commands, functions, protocols and objects that programmers can use
# to create software or interact with an external system

# The API is an interface or a barrier between your program and the external system
# The API allows you to structure your request the way the website understands, or accepts

# Kind of like a restaurant, you do not go in one and start taking things from the cupboard right?
# You see the menu to order, that is their prescribed way of ordering, also shows what you can and cannot order
# An API is just that, lets you understand what you can and cannot order/request


# 296 API Endpoints and Making API Calls

# API Endpoints -
# A url that has the location of the data that you want
# api.coinbase.com

# API Requests -
# This is the request that you make to pull the data out of the external system
#
# There are some requests for which you need to go through some form of authentication
# And there are some requests that do not require an authentication

# One of the common APIs is the ISS current location viewer
# Here - http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# When you go to the website, you will see the API endpoint
# http://api.open-notify.org/iss-now.json

# You can simply paste the API endpoint in the browser, and it will give you a simple output that shows ISS location
# The API endpoint is in JSON format
# Now let's say we want the API endpoint output in a clean dictionary format, easy to read and all

# You can do it using requests

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

# <Response [200]>
# we get the response code, not the contents in an clean dict format
# how to get the response in a clean dict format?


# 297 Working with Responses_ HTTP Codes, Exceptions & JSON Data

# There can be various types of response codes
# 404 - The thing you are looking for does not exist

# There are ways you can know what the response code actually means
# 1XX - Hold On
# 2XX - Success
# 3XX - Go Away, you do not have access
# 4XX - You screwed up
# 5XX - I(website/server) screwed up

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
# 200

import requests

response = requests.get(url="http://api.open-notify.org/is-now.json")
print(response.status_code)
# 404
# that url contains an intentional typo

# For a full rundown of all possible types of response codes, visit - https://httpstatuses.com/

# To get the response code in the code without having to visit the website, use raise_for_status method
import requests

response = requests.get(url="http://api.open-notify.org/is-now.json")
print(response.raise_for_status())

# requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://api.open-notify.org/is-now.json

# How do we get the data stored in JSON?
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

data = response.json()
print(data)
print(data['iss_position'])
print(data['iss_position']['longitude'])

# {'message': 'success', 'timestamp': 1685229358, 'iss_position': {'latitude': '30.2115', 'longitude': '-12.9513'}}
# {'latitude': '30.2115', 'longitude': '-12.9513'}
# -12.9513

# to pretty print, we can use the json module
# json.dumps() to pretty print
# the dumps() method returns a json formatted string from the json object
# the indent parameter is used to define the indent level

import requests
import json

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
formatted_data = json.dumps(data, indent=1)
print(formatted_data)
# {
#  "message": "success",
#  "timestamp": 1685229854,
#  "iss_position": {
#   "latitude": "6.1757",
#   "longitude": "7.4952"
#  }
# }

# Now, you have the longitude and latitude, right?
# what if we want to see where in the world map that is?
# latlong.net > geographic tools > lat and long to address > paste the coordinates


# 298 Challenge - Build a Kanye Quotes App using the Kanye Rest API

# you have a kanye quotes api
# you have a basic tkinter app interface with a button
# all you have to do is everytime you press the button the text in the screen will change to one of kanye's quotes

from tkinter import *
import requests

def get_quote():
    # this is where you need to code
    response = requests.get('https://api.kanye.rest')
    data = response.json()
    canvas.itemconfig(quote_text, text=data['quote'], font=("Arial", 15, "bold"))



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()


# 299 Understand API Parameters_ Match Sunset Times with the Current Time

# APIs also have parameters, a way for APIs to have inputs
# With these inputs, we tell the API to give us specific information
# Think about the previous example
# We worked with the entire json and got the longitude and latitude data
# We could pass in parameters to get these data at the API level

# The ISS API was quite simple, it did not require any parameters
# There is another API called the sunrise and sunset API that takes in locational parameters
# and gives the time the sun rises and sets in that location

# Just like a function, in APIs we have required and optional parameters
# The optional ones always have a default value, for example date, if emmpty, it will take today's date


# Second response to get the sunrise and sunset data in my city
#
parameters = {
    "lat": 23.810331,
    "lng": 90.412521,
}
# These are Dhaka's latitudes and longitudes

response2 = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response2.raise_for_status()

# timestamp - 09:47

print(data2)
# {'results': {'sunrise': '5:52:33 AM', 'sunset': '6:01:58 PM', 'solar_noon': '11:57:15 AM', 'day_length': '12:09:25', 'civil_twilight_begin': '5:31:28 AM', 'civil_twilight_end': '6:23:03 PM', 'nautical_twilight_begin': '5:05:37 AM', 'nautical_twilight_end': '6:48:54 PM', 'astronomical_twilight_begin': '4:39:41 AM', 'astronomical_twilight_end': '7:14:50 PM'}, 'status': 'OK'}

# if you want to the data in a formatted way, use json.dumps()
formatted_data2 = json.dumps(data2, indent=1)
print(formatted_data2)
# {
#  "results": {
#   "sunrise": "5:52:33 AM",
#   "sunset": "6:01:58 PM",
#   "solar_noon": "11:57:15 AM",
#   "day_length": "12:09:25",
#   "civil_twilight_begin": "5:31:28 AM",
#   "civil_twilight_end": "6:23:03 PM",
#   "nautical_twilight_begin": "5:05:37 AM",
#   "nautical_twilight_end": "6:48:54 PM",
#   "astronomical_twilight_begin": "4:39:41 AM",
#   "astronomical_twilight_end": "7:14:50 PM"
#  },
#  "status": "OK"
# }

# if you want to the data in a formatted way, use the full request in the url
# https://api.sunrise-sunset.org/json?lat=23.810331&lng=90.412521


# 300 ISS Overhead Notifier Project - Challenge & Solution

# timestamp - 03:00

# TODO 0 Import modules and declare variables
import requests
import json
import datetime as dt
import smtplib

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
# TODO 8a - Make the code run continuously to see if the ISS is overhead
while True:
    import time
    time.sleep(300)
    if iss_in_range() and is_night_time():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="rafi.abdullah.112358@gmail.com",
                                msg=message)


