import requests
sheety_endpoint = "https://api.sheety.co/ea8ab6e9bfe6ae6a2026b7f9c26986e1/flightFinder/prices"
sheety_endpoint_users = "https://api.sheety.co/ea8ab6e9bfe6ae6a2026b7f9c26986e1/flightFinder/users"
# To retrieve rows from your sheet, perform a GET request to the endpoint. This will return all records in your sheet.
# If you want to return a specific record, append the object ID (which is just the row number) to the endpoint URL.
sheety_response = requests.get(url=sheety_endpoint)
print(sheety_response.json())
sheety_response2 = requests.get(url=f"{sheety_endpoint}/3")
print(sheety_response2.json())
my_price = sheety_response2.json()["price"]["lowestPrice"]
print(my_price)
sheety_response_users = requests.get(url=sheety_endpoint_users)
print(sheety_response_users.json())
# for i in sheety_response.json()["sheet1"]:
#     print(i["city"], i["lowestPrice"])


# to get the city names to pass into the IATA class -
for i in sheety_response.json()["prices"]:
    print(i["city"])

# Plug in the IATA in the rows -
# couple of things before we construct the sheety contents -
# Sheety expects your record to be nested in a singular root property named after your sheet.
# For example if your endpoint is named emails, nest your record in a property called email.
# So if our endpoint ends in "workouts", it should be changed to "workout"
# Also, all the parameters have to be lower case, despite how they are written in the excel sheet
# Lastly, sheety camelCases all JSON keys, so a header named "First Name" will become "firstName".
update_url = f"{sheety_endpoint}/2"
data = {
    'price': {
        "iataCode": "data"
    }
}
update_response = requests.put(url=update_url, json=data)
print("response.status_code =", update_response.status_code)
print(update_response.text)

# So, updating the IATA in the google sheet would look like this -


def insert_iata():
    for i in sheety_response.json()["sheet1"]:
        city_name = (i["city"])
        ID = (i["id"])
        iata = iata_by_city(city_name)
        update_url = f"{sheety_endpoint}/{ID}"
        data = {
            'sheet1': {
                "iataCode": iata
            }
        }
        requests.put(url=update_url, json=data)

def get_my_price():
