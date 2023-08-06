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
