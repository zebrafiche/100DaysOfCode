# 335 Day 39 Goals_ what you will make by the end of the day

# We will basically use a combination of different APIs to develop a cheap flight finder
# This is a two part project -
# In this part (part one), we are going to develop this flight finder just for ourselves
# And in the next part (part two) we will develop this to allow users to sign up to this service

# Step 1 - We will use a google sheet to set the destination and the cutoff price
# Step2 - We will use a flight search API to pull data from the google sheet and look for matches
# Step 3 - When there are flights marching our location and cut off price, it will send us an SMS using the Twillio API


# 336 Step 1 - Choose Your Path and Download the Starting Project
# First, I have created a new google sheet named "Flight Finder"

# 1. Log into Sheety with your Google Account (the same account that owns the Google Sheet you copied in step 1).
# Make sure the email matches between your Google Sheet and Sheety Account. e.g.
# 2. In your project page, click on "New Project" and create a new project in Sheety with the name "Flight Finder"
# and paste in the URL of your own "Flight Finder" Google Sheet.
# 3. Enable GET, since we only want to retrieve data from the sheet, we will only need the GET feature.
import requests
sheety_endpoint = "https://api.sheety.co/a0892b931bb7f18a9dabc132e4f37037/flightFinder/sheet1"
# To retrieve rows from your sheet, perform a GET request to the endpoint. This will return all records in your sheet.
# If you want to return a specific record, append the object ID (which is just the row number) to the endpoint URL.
sheety_response = requests.get(url=sheety_endpoint)
print(sheety_response.text)
# the output will be something like a dictionary named after the sheet (sheet1), containing a list of dictionaries
# Each dict represent the contents of each row
# {'sheet1': [
#     {'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
#     {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
#     {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
#     {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
#     {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
#     {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
#     {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
#     {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
#     {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}

# to get the lowest price for each city, perform -
for i in sheety_response.json()["sheet1"]:
    print(f'{i["city"], i["lowestPrice"]}')
# Paris 54
# Berlin 42
# Tokyo 485
# Sydney 551
# Istanbul 95
# Kuala Lumpur 414
# New York 240
# San Francisco 260
# Cape Town 378

a = 2
print(f"{a}")