import everyday
import get_price
import mail_me

url = input('Enter the Amazon url or camel url of the product you want to set this up for: ')
target_price = input('Enter your target price for this item: ')

while True:
    if everyday.is_it_0500():
        get_price.scrape(url)
        if get_price.within_budget(item_price=target_price):
            mail_me.compose_msg(url, get_price.price)
            mail_me.send_mail()
