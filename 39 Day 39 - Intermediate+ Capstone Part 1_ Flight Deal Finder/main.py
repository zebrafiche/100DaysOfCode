import data_manager
import flight_search
import flight_data
import send_mail

sheet = data_manager.DataManager()
search = flight_search.FlightSearch()
data = flight_data.FlightData()
mail = send_mail.send_mail()

# Step 1 - Get city names
sheet.get_city_names()
# Step 2 - Iterate through the city names to insert IATA
for i in sheet.city_names:
    sheet.insert_iata(i)
# Step 3 - Get the prices
    sheet.get_my_price(i)
    data.get_prices(i)
# Step 4 - If prices are lower than your prices, draft a message
    data.compare_prices(sheet.my_price)
# Step 5 - Send message via email
mail.send_a_mail()
