import datetime


class dateTracker:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.six_months = self.today + datetime.timedelta(days=365.25 / 2)
        self.date_today = self.today.strftime("%d/%m/%Y")
        self.date_six_months = self.six_months.strftime("%d/%m/%Y")

