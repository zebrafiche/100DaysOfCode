import smtplib
import os
import data_manager
import requests

my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("PASS")
app_password = os.environ.get("APP_PASS")
sheet = data_manager.DataManager()


class send_mail:
    def __init__(self):
        self.connection = smtplib.SMTP_SSL('smtp.gmail.com')
        # Got [WinError 10060] (connection attempt failed) with smtplib.SMTP('smtp.gmail.com')
        # Changed it to smtplib.SMTP_SSL('smtp.gmail.com') (Stack Overflow) & commented out self.connection.starttls()

    # For Step 5 - Get the message containing all details of flights that are under the budget, and send all a mail
    def send_a_mail(self, message):
        # self.connection.starttls()
        self.connection.login(user=my_email, password=app_password)
        users_response = requests.get(url=sheet.endpoint_users)
        for i in users_response.json()["users"]:
            username = i['firstName']
            usermail = i['email']
            self.connection.sendmail(from_addr=my_email,
                                     to_addrs=usermail,
                                     msg=f"Subject: Deal Alert for {username}"
                                         f"\n\nHave a look at this"
                                         f"\n\n{message}"
                                         f"\n\nHave a great day!"
                                         f"\n\nRegards."
                                         f"\nRafi")
