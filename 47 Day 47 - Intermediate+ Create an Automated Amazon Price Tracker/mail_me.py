import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
SENDER = EMAIL_ADDRESS
RECEIVER = 'rafi.abdullah.112358@gmail.com'

msg = EmailMessage()


def compose_msg(url, price):
    global msg
    msg['Subject'] = 'Price Drop Alert'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECEIVER
    msg.set_content(f'Your favorite product just got its price slashed. It is now {price}.\n'
                    f'Grab it here -\n{url}')


def send_mail():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
