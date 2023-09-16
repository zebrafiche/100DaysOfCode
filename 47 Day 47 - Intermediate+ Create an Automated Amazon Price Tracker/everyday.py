import datetime

now = datetime.datetime.now()
print(now)


def is_it_0500():
    if now.hour == 5:
        return True
