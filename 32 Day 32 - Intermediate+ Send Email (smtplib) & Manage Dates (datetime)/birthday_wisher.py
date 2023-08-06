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
