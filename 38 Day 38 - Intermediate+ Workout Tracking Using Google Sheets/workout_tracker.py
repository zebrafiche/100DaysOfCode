import requests
import datetime
from requests.auth import HTTPBasicAuth
import os

# store the ID and api key as environment variables
nutritionix_app_ID = os.environ.get('nutritionix_app_ID')
nutritionix_api = os.environ.get('nutritionix_api')

# store the api endpoint
nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# construct the header
header = {
    'x-app-id': f"{nutritionix_app_ID}",
    'x-app-key': f"{nutritionix_api}",
    # 'Content-Type': 'json', although the doc says this should be here, stack overflow says it shouldn't
}

# construct the query
query_config = {
    "query": f"{input('What and how much did you do today?: ')}",
    "gender": "male",
    "weight_kg": 95,
    "height_cm": 177.8,
    "age": 33
}

# send the request
# N.B - You do not use params in requests.post(). Since YOU are sending data, you use json as an argument
nutritionix_response = requests.post(url=nutritionix_endpoint, json=query_config, headers=header)
print(nutritionix_response.text)
# What and how much did you do today?: cycled for 10 minutes
# {"exercises":[{
#     "tag_id":5,
#     "user_input":"cycled",
#     "duration_min":10,
#     "met":10,
#     "nf_calories":158.33,
#     "photo":{"highres":"https://d2xdmhkmkbyw75.cloudfront.net/exercise/5_highres.jpg",
#              "thumb":"https://d2xdmhkmkbyw75.cloudfront.net/exercise/5_thumb.jpg","is_user_uploaded":false},
#     "compendium_code":1040,
#     "name":"road cycling",
#     "description":null,
#     "benefits":null}]
# }
print(f'{nutritionix_response.json()["exercises"][0]["name"]}')
# jogging

# store sheety endpoint to insert new rows
# Sheety API URLs are made up three core components: username, project name, and sheet name.
# https://api.sheety.co/username/projectName/sheetName
# You can find the exact URLs for your sheet in the Dashboard -
# https://api.sheety.co/a0892b931bb7f18a9dabc132e4f37037/workoutTracking/workouts
sheety_endpoint = os.environ.get("sheety_endpoint")

# construct the sheety contents, delineate sheet name, followed by column names
# to insert the day's date into the sheety contents, work with datetime first
today = datetime.datetime.now()
today_time = today.strftime('%H:%M:%S')

# couple of things before we construct the sheety contents -
# Sheety expects your record to be nested in a singular root property named after your sheet.
# For example if your endpoint is named emails, nest your record in a property called email.
# So since our endpoint ends in "workouts", it should be changed to "workout"
# Also, all the parameters have to be lower case, despite how they are written in the excel sheet
sheety_contents = {
    'workout': {
        'date': f'{today.day}/{today.month}/{today.year}',
        'time': f'{today_time}',
        # we cannot do response.text because that generates a str output, getting the name of the exercise is a hassle
        # instead, we will do response.json() to get the json output, and use key values to access the exercise name
        'exercise': f'{nutritionix_response.json()["exercises"][0]["name"]}',
        'duration': f'{nutritionix_response.json()["exercises"][0]["duration_min"]}',
        'calories': f'{nutritionix_response.json()["exercises"][0]["nf_calories"]}',
    }
}

# make the request
# but before that, authenticate your API so others cannot access the sheet
user = os.environ.get("user")
password = os.environ.get("password")
basic = HTTPBasicAuth(username=user, password=password)

sheety_response = requests.post(url=sheety_endpoint, json=sheety_contents, auth=basic)
sheety_response.raise_for_status()
# you can see that the sheet gets updated with a new row, noice
