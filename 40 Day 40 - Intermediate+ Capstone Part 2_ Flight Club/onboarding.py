

class UserOnboard:
    def __init__(self):
        self.first_name = input("Welcome to the Flight Club.\n"
                                "We'll find the best flight deals for you.\n"
                                "What is your first name?")
        self.last_name = input("What is your last name?")
        self.mail_address = input("Enter your email.")
        self.mail_address_verify = input("Type your email again.")

    def verify_emails(self):
        if self.mail_address == self.mail_address_verify:
            print("Welcome to the club")
            return True
        else:
            print("The mail addresses do not match")
            return False
