# 286 Day 32 Goals_ what we will make by the end of the day

# Email SMTP and the datetime module

# We will use these tools to create a system in Python that will send an automated email
# to our friends on their birthdays

# datetime - to get dates in python
# SMTP - To use the dates to figure out if today is someone's birthday


# 288 How to Send Emails with Python using SMTP

# How do emails work
# Let's say that I emailed a friend
# I use gmail, my friend uses yahoo
# The mail will be passed through the gmail mail server to the yahoo mail server
# There it gets stored until my friend logs on to his computer and opens yahoo, whereby the mail gets delivered
# The entire thing is done using SMTP - Simple Mail Transfer Protocol

# To do this it is better to open a fresh new gmail account and a fresh new yahoo account
# The accounts should be less secure to help with our programming, that is another reason to open new accounts

# IMPORT MODULE
import random
import smtplib

my_email = 'rough.rafi@gmail.com'
my_password = 'fotkabazz1123581321'
app_password = 'uzdalqmxwenwmvmy'


# SET UP CONNECTION
connection = smtplib.SMTP('smtp.gmail.com')

# for gmail it is smtp.gmail.com
# for hotmail it is smtp.live.com
# for yahoo it is smtp.mail.yahoo.com
# if you have a different email provider other than these then just google it

# SECURE THE CONNECTION
connection.starttls()
# tls refers to "Transport Layer Security", this makes the connection secure, so no one that can read the mail

# LOGIN
connection.login(user=my_email, password=my_password)

# SEND THE MAIL
connection.sendmail(from_addr=my_email, to_addrs="rafi.abdullah.112358@gmail.com",
                    msg="Hello how are ye?")

# CLOSE THE CONNECTION
connection.close()

# we get a number of errors
# gmail blocks the connection, because by default, gmail does not let just anybody access mail

# head over to your google account
# disable -
# 1. use your phone to sign in
# 2. 2 step verification
# turn on "less secure app access"

# However, it seems that google has a newer way of allowing this
# App passwords
# An app password is a 16-digit passcode that gives another app or device permission to access your Google Account.
# App passwords can only be used with accounts that have 2-Step Verification turned on.
# App passwords let you sign in to your Google Account from apps on devices that don't support 2-Step Verification.
# Use the instructions in the link provided in the error
# Replace your password with the 16-character password generated for PyCharm

# After replacing my_password with app_password, I get the mail sent

# LET'S SEND ANOTHER
import smtplib

my_email = 'rough.rafi@gmail.com'
my_password = 'fotkabazz1123581321'
app_password = 'uzdalqmxwenwmvmy'
message = 'Subject: Happy Birthday!!!\n\nHello, wishing you a very happy birthday\nRegards,\nRafi'

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_email, password=app_password)
connection.sendmail(from_addr=my_email,
                    to_addrs="rafi.abdullah.112358@gmail.com",
                    msg=message)
connection.close()

# success!

# we can also bypass the connection.close() if we use the with keyword, just like we used when opening files
import smtplib

my_email = 'rough.rafi@gmail.com'
my_password = 'fotkabazz1123581321'
app_password = 'uzdalqmxwenwmvmy'
message = 'Subject: Happy Birthday!!!\n\nHello, wishing you a very happy birthday\n\nRegards,\n\nRafi'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="rafi.abdullah.112358@gmail.com",
                        msg=message)


# 289 Working with the datetime Module

# you can use datetime to get the date from the computer
import datetime
# now get to the datetime class inside the datetime module
datetime.datetime()
# now this is confusing, right?

# so do this
import datetime as dt
# get to the datetime class, and get to the method now(), that gives today's date and time
now = dt.datetime.now()
print(now)
# 2023-05-24 05:26:51.167003

# getting to various properties of now()
year = now.year
print(year)
# 2023
print(type(year))
# <class 'int'>
print(type(now))
# <class 'datetime.datetime'>
day_of_the_week = now.weekday()
print(day_of_the_week)
# 2 (week starts from Monday)

# how to create a datetime object, capturing a particular date?
date_of_birth = dt.datetime(year=1989, month=12, day=14)
print(date_of_birth)
# 1989-12-14 00:00:00
# specify the time -
date_of_birth = dt.datetime(year=1989, month=12, day=14, hour=9)
print(date_of_birth)
# 1989-12-14 09:00:00


# 290 Challenge 1 - Send Motivational Quotes on Mondays via Email

# 1. Turn every line from a txt file into a list
with open('quotes.txt') as file:
    quotes_list = file.readlines()
print(quotes_list)
# list created

# 2. Strip the newline characters
for i in quotes_list[0:5]:
    print(i.strip())
# "When you arise in the morning think of what a privilege it is to be alive, to think, to enjoy, to love..."  - Marcus Aurelius
# "Either you run the day or the day runs you." - Jim Rohn
# "Mondays are the start of the work week which offer new beginnings 52 times a year!" - David Dweck
# "You've got to get up every morning with determination if you're going to go to bed with satisfaction." - George Lorimer
# "Be miserable. Or motivate yourself. Whatever has to be done, it's always your choice." - Wayne Dyer

# 3. Check if it is Wednesday using datetime
if day_of_the_week == 3:
    # code

# 4. Send a mail to yourself on Wednesdays/Thursdays
import random
random_message = random.choice(quotes_list)
print(random_message.strip())
connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_email, password=app_password)
connection.sendmail(from_addr=my_email,
                    to_addrs="rafi.abdullah.112358@gmail.com",
                    msg=random_message.strip())
connection.close()

# timestamp - 02:00

# 5. Put it all together

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




# 291 Automated Birthday Wisher Project Challenge

# This is what I came up with

# Extra Hard Starting Project #

# Todo 0. Import the modules
import pandas
import datetime as dt
import os
import random
import smtplib

# Todo 1. Update the birthdays.csv

# Done

# Todo 2. Read the CSV
birthdays = pandas.read_csv('birthdays.csv')
# print(birthdays)
#        name                  email  year  month  day
# 0      Rafi   rough.rafi@gmail.com  1989      5   25
# 1    Teetly   rough.rafi@gmail.com  1989      5   25
# 2  Dingding    msharat22@gmail.com  1990     12   21
# 3    My Man   rough.rafi@gmail.com  1989     12   14

# Todo 3. Check if today matches a birthday in the birthdays.csv

# Todo 3a. Use datetime to get today's date
now = dt.datetime.now()
now_month = now.month
now_day = now.day

# Todo 3b. Use that date to filter the rows from the data
birthdays_today = birthdays.query(f"month == {now_month} & day == {now_day}")
# print(birthdays_today)
#      name                 email  year  month  day
# 0    Rafi  rough.rafi@gmail.com  1989      5   25
# 1  Teetly  rough.rafi@gmail.com  1989      5   25


# Todo 3c. Get the names from the rows
names = birthdays_today.name
# print(names)
# 0      Rafi
# 1    Teetly
# Name: name, dtype: object

# Todo 4. If step 4 is true,
#  pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# Todo 4a. Generate a list of files from the directory
files_list = os.listdir("./letter_templates")
# print(files_list)
# ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

# Todo 4b. Pick a random letter
chosen_letter = random.choice(files_list)

# Todo 4c. Get the letter's contents
with open(f"./letter_templates/{chosen_letter}") as file:
    mail_text = file.read()
    revised_mail_text = mail_text.replace('Angela', "Rafi")
    # print(revised_mail_text)

# Happy birthday! Have a wonderful time today and eat lots of cake!
# Lots of love,
# Rafi

# Todo 4d. Replace the name(s)
# for name in names:
#     new_mail_text = revised_mail_text.replace('[NAME]', name)
# commenting this out because this is going to merge with the next step

# Todo 5. Send the letter generated in step 3 to that person's email address.

my_email = 'rough.rafi@gmail.com'
my_password = 'fotkabazz1123581321'
app_password = 'uzdalqmxwenwmvmy'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_password)
    for name in names:
        new_mail_text = revised_mail_text.replace('[NAME]', name)
        connection.sendmail(from_addr=my_email,
                            to_addrs="rafi.abdullah.112358@gmail.com",
                            msg=f"Subject: Happy Birthday!!!\n\n{new_mail_text}")


# 292 Solution & Walkthrough for the Automated Birthday Wisher

# Angels's Solution

#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )


# 293 Run Your Python Code in the Cloud!

# Go to python anywhere
# Create a free account
# Upload your files in the same way that they are organized in the project folder
# Click Bask
# Once you see the $ sign, type "python3 birthday_wisher.py"
# If you see any login error, go to the link provided in the error to fix login issues
# Run Again
# Lastly, schedule, provide a time and a command ("python3 birthday_wisher.py")
# That is it, on the stipulated time it will run your command every day
