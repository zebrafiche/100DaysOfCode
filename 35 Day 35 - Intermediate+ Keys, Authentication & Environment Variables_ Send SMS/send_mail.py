import smtplib

my_email = 'rough.rafi@gmail.com'
my_password = 'fotkabazz1123581321'
app_password = 'uzdalqmxwenwmvmy'


class sm:
    def __init__(self):
        self.connection = smtplib.SMTP('smtp.gmail.com')

    def send_a_mail(self, message):
        self.connection.starttls()
        self.connection.login(user=my_email, password=app_password)
        self.connection.sendmail(from_addr=my_email,
                                to_addrs="rafi.abdullah.112358@gmail.com",
                                msg=f"Subject: Weather Update"
                                    f"\n\nHave a look at today's weather forecasts"
                                    f"\n\n{message}"
                                    f"\n\nHave a great day!"
                                    f"\n\nRegards."
                                    f"\nRafi")

