# Now for the tequila API
import requests

api_endpoint = "https://api.tequila.kiwi.com"
apikey = "Cf93SFmKDorpk6zeU4TT28CAyeAZ6339"
city_name = "Kolkata"
header = {
    "apikey": apikey
}

query = {
    "term": f"{city_name}",
    "location_types": "airport",
    "locale": "en-US",
}
tequila_response = requests.get(url=f"{api_endpoint}/locations/query", headers=header, params=query)
print(tequila_response.json())
print(tequila_response.json()["locations"][0]['city']['code'])


def iata_by_city(city_name):
    query = {
        "term": f"{city_name}",
        "location_types": "airport",
        "locale": "en-US",
    }
    tequila_response = requests.get(url=f"{api_endpoint}/locations/query", headers=header, params=query)
    return tequila_response.json()["locations"][0]['city']['code']


iata_by_city(city_name=city_name)

# tequila_response = requests.get(url=f"{api_endpoint}/locations/query", headers=header, params=query)
# # requests.get always use params as an argument, requests.post/requests.put use json
# print(tequila_response.text)
# # to get the IATA -
# IATA = tequila_response.json()["locations"][0]['city']['code']

