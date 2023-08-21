# Now for the tequila API
import requests
import date_tracker

date = date_tracker.dateTracker()
api_endpoint = "https://api.tequila.kiwi.com"
apikey = "Cf93SFmKDorpk6zeU4TT28CAyeAZ6339"

header = {
    "apikey": apikey
}

query = {
    "fly_from": "DAC",
    "fly_to": "CCU",
    "date_from": f"{date.date_today}",
    "date_to": f"{date.date_six_months}",
    "price_from": 10,
    "price_to": 150,
    "adults": 2,
    "curr": "USD"

}

tequila_response = requests.get(url=f"{api_endpoint}/v2/search", headers=header, params=query)
# requests.get always use params as an argument, requests.post/requests.put use json
print(tequila_response.text)
# to get the price -
for i in tequila_response.json()["data"]:
    print(i["local_arrival"])
    print((i["price"]))


# get the price by the iata -
def price_by_iata(iata):
    query = {
        "fly_from": "DAC",
        "fly_to": f"{iata}",
        "date_from": "10/07/2023",
        "date_to": "10/12/2023",
        "price_from": 100,
        "price_to": 200,
        "adults": 2,
        "curr": "USD"

    }
    response = requests.get(url=f"{api_endpoint}/v2/search", headers=header, params=query)
    print(response.text)

# Logic -
#     if tequila prices is less than your prices:
#         send a mail
#         include date, destination, airline, price

price_by_iata("CCU")

message =

for i in sheety_response.json()["sheet1"]:
    city_name = i["city"])
    lowest_price = i["city"], i["lowestPrice"]
    # iata = iata_by_city(city_name)

    def price_by_iata(iata):
        iata = iata_by_city(city_name)
        query = {
            "fly_from": "DAC",
            "fly_to": f"{iata}",
            "date_from": "10/07/2023",
            "date_to": "10/12/2023",
            "price_from": 100,
            "price_to": 200,
            "adults": 2,
            "curr": "USD"

        }
        tequila_response = requests.get(url=f"{api_endpoint}/v2/search", headers=header, params=query)

    for j in tequila_response.json()["data"]:
        if (j["price"]) <= lowest_price:
            date = j["local_arrival"]
            destination = f"{j['cityTo']}", {j['cityCodeTo']}
            airline = j['airlines']
            price = j["price"]
            message.append = f"{date}\n{destination}\n{airline}\n{price}\n\n"
