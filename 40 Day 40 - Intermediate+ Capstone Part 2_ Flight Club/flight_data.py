import requests
import flight_search
import date_tracker

search = flight_search.FlightSearch()
date = date_tracker.dateTracker()


class FlightData:
    def __init__(self):
        self.endpoint = "https://api.tequila.kiwi.com"
        self.apikey = "Cf93SFmKDorpk6zeU4TT28CAyeAZ6339"

        self.header = {
            "apikey": self.apikey
        }
        self.message = 'Prices:\n\n'
        self.response = None

    # For Step 3 - Get the data that contains prices for all the flights within the stipulated date
    def get_prices(self, city_name):
        search.iata_by_city(city_name)
        query = {
            "fly_from": "DAC",
            "fly_to": f"{search.iata}",
            "date_from": f"{date.date_today}",
            "date_to": f"{date.date_six_months}",
            "price_from": 100,
            "price_to": 200,
            "adults": 2,
            "curr": "USD"

        }
        self.response = requests.get(url=f"{self.endpoint}/v2/search", headers=self.header, params=query)
        # print(self.response.status_code)
        # print(self.response.json())

    # For Step 4 - From the data collected in Step 3 - get prices, if any price is lower/equal to my price,
    # store the details in a msg
    def compare_prices(self, my_price):
        for j in self.response.json()["data"]:
            if (j["price"]) <= my_price:
                travel_date = j["local_arrival"]
                destination = f"{j['cityTo']}", {j['cityCodeTo']}
                airline = j['airlines']
                price = j["price"]
                link = j["deep_link"]
                self.message += f"{travel_date}\n" \
                                f"{destination}\n" \
                                f"{airline}\n" \
                                f"{price}\n" \
                                f"{link}\n\n"
