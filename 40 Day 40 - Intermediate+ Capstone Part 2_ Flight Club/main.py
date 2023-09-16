import data_manager
import flight_search
import flight_data
import send_mail
import onboarding

sheet = data_manager.DataManager()
search = flight_search.FlightSearch()
data = flight_data.FlightData()
mail = send_mail.send_mail()

# Step -1 - Ask if it is a new user sign_up, in which case initialize the UserOnboard() class
if input("New user sign up?(Y/N)") == 'Y':
    user = onboarding.UserOnboard()
# Step 0 - Onboard new users if verification successful
    if user.verify_emails():
        sheet.add_row(user.first_name, user.last_name, user.mail_address)
# Step 1 - Get city names
sheet.get_city_names()
# Step 2 - Iterate through the city names to insert IATA
for i in sheet.city_names:
    sheet.insert_iata(i)
# Step 3 - Get the prices
    sheet.get_my_price(i)
    print(sheet.my_price)
    data.get_prices(i)
# Step 4 - If prices are lower than your prices, draft a message
    data.compare_prices(sheet.my_price)
# Step 5 - Send message via email to the users
mail.send_a_mail(data.message)
