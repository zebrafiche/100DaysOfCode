import requests
import flight_search

search = flight_search.FlightSearch()


class DataManager:
    def __init__(self):
        self.endpoint = "https://api.sheety.co/eba3e95236c775b0a64eab76b434f3a6/copyOfFlightDeals/prices"
        self.response = requests.get(url=self.endpoint)
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
        for i in self.response.json()["prices"]:
            city_name = (i["city"])
            self.city_names.append(city_name)

    # For Step 3 - Get my preferred price for a city, from the google sheet
    def get_my_price(self, city_name):
        ID = self.city_names.index(city_name) + 2
        price_url = f"{self.endpoint}/{ID}"
        price_response2 = requests.get(url=f"{price_url}")
        self.my_price = price_response2.json()["price"]["lowestPrice"]
