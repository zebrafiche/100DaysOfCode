import requests
import flight_search

search = flight_search.FlightSearch()


class DataManager:
    def __init__(self):
        self.endpoint = "https://api.sheety.co/ea8ab6e9bfe6ae6a2026b7f9c26986e1/flightFinder/prices"
        self.endpoint_users = "https://api.sheety.co/ea8ab6e9bfe6ae6a2026b7f9c26986e1/flightFinder/users"
        # self.response = requests.get(url=self.endpoint)
        self.city_names = []
        self.my_price = 0

    # For Step 2 - Insert IATA by passing the city_name to the search.iata_by_city() function
    def insert_iata(self, city_name):
        ID = self.city_names.index(city_name) + 2
        update_url = f"{self.endpoint}/{ID}"
        search.iata_by_city(city_name)
        data = {
            'price': {
                "iataCode": search.iata
            }
        }
        requests.put(url=update_url, json=data)

    # For Step 1 - Get city names from the google sheet
    def get_city_names(self):
        names_response = requests.get(url=self.endpoint)
        for i in names_response.json()["prices"]:
            city_name = (i["city"])
            self.city_names.append(city_name)

    # For Step 3 - Get my preferred price for a city, from the google sheet
    def get_my_price(self, city_name):
        ID = self.city_names.index(city_name) + 2
        price_url = f"{self.endpoint}/{ID}"
        price_response2 = requests.get(url=f"{price_url}")
        self.my_price = price_response2.json()["price"]["lowestPrice"]

    # For Step 0 - get the user credentials from onboarding.py and add them to a new row in sheety
    def add_row(self, first_name, last_name, mail_address):
        user_data = {
            'user': {
                "firstName": f"{first_name}",
                "lastName": f"{last_name}",
                "email": f"{mail_address}",
            }
        }
        requests.post(url=self.endpoint_users, json=user_data)



