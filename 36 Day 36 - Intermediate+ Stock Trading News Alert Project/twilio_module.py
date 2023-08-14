from twilio.rest import Client
import os

# saved twilio sid and auth token as environment variables


class tw:
    def __init__(self):
        self.client = Client(os.environ.get('TWILIO_SID'), os.environ.get('TWILIO_AUTH_TOKEN'))

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="+13613154628",
            to="+8801681407930"
        )
        print(message.status)
