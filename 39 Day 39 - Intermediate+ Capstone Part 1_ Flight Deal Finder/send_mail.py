import smtplib
import flight_data
import os

my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASS")
app_password = os.environ.get("APP_PASS")

data = flight_data.FlightData()


class send_mail:
    def __init__(self):
        self.connection = smtplib.SMTP_SSL('smtp.gmail.com')
        # Got [WinError 10060] (connection attempt failed) with smtplib.SMTP('smtp.gmail.com')
        # Changed it to smtplib.SMTP_SSL('smtp.gmail.com') (Stack Overflow) & commented out self.connection.starttls()

    # For Step 5 - Get the message containing all details of flights that are under my budget, and send me a mail
    def send_a_mail(self):
        # self.connection.starttls()
        self.connection.login(user=my_email, password=app_password)
        self.connection.sendmail(from_addr=my_email,
                                 to_addrs=os.environ.get("MY_EMAIL2"),
                                 msg=f"Subject: Deal Alert"
                                     f"\n\nHave a look at this"
                                     f"\n\n{data.message}"
                                     f"\n\nHave a great day!"
                                     f"\n\nRegards."
                                     f"\nRafi")
