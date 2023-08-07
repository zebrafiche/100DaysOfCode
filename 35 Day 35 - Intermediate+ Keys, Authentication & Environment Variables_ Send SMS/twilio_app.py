from twilio.rest import Client


class twilio:
    def __init__(self):
        self.account_sid = "AC11d33501f25cae1f5eea614843172b76"
        self.auth_token = os.environ["ad15cc22fef5353bbce8d38a6c99698d"]

    def send_text(self, message):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=message,
            from_="+13613154628",
            to="+8801681407930"
        )
        print(message.status)