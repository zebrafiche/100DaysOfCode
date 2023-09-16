import requests


class FlightSearch:
    def __init__(self):
        self.endpoint = "https://api.tequila.kiwi.com"
        self.apikey = "Cf93SFmKDorpk6zeU4TT28CAyeAZ6339"

        self.header = {
            "apikey": self.apikey
        }
        self.iata = str()

    # For Step 2 - Get IATA codes from city_names
    def iata_by_city(self, city_name):
        query = {
            "term": f"{city_name}",
            "location_types": "airport",
            "locale": "en-US",
        }
        tequila_response = requests.get(url=f"{self.endpoint}/locations/query", headers=self.header, params=query)
        self.iata = tequila_response.json()["locations"][0]['city']['code']
