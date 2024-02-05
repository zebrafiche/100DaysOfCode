import smtplib


class Gmailer:
    def __init__(self):
        self.my_email = 'rough.rafi@gmail.com'
        self.my_password = 'fotkabazz1123581321'
        self.app_password = 'uzdalqmxwenwmvmy'
        self.connection = smtplib.SMTP('smtp.gmail.com')
        self.message = None
        self.connection.starttls()

    def draft_msg(self, name, email, phone, msg):
        self.message = f'Subject: New Form!!!\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {msg}\n\n'

    def send(self):
        self.connection.login(user=self.my_email, password=self.app_password)
        self.connection.sendmail(from_addr=self.my_email,
                            to_addrs="rafi.abdullah.112358@gmail.com",
                            msg=self.message)
        # self.connection.close()