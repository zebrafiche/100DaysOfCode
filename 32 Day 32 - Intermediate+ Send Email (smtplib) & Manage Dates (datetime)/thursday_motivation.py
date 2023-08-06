import datetime as dt
import random
import smtplib

my_email = 'rough.rafi@gmail.com'
my_password = 'fotkabazz1123581321'
app_password = 'uzdalqmxwenwmvmy'

with open('quotes.txt') as file:
    quotes_list = file.readlines()

now = dt.datetime.now()
day_of_the_week = now.weekday()
if day_of_the_week == 3:
    random_message = random.choice(quotes_list)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email,
                        to_addrs="rafi.abdullah.112358@gmail.com",
                        msg= f"Subject: Thursday Motivation"
                             f"\n\nHere's your motivation for the day"
                             f"\n\n{random_message.strip()}"
                             f"\n\nHave a great day!"
                             f"\n\nRegards."
                             f"\nRafi")


