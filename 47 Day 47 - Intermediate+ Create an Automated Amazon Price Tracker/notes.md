### 408 Day 47 Goals_ what you will make by the end of the day

So today we will build an Amazon price tracking bot.

We will have a product link, the bot will scrape the price from that link and send us an email if the price 
is below our target price.


Steps
1. Get the url of the product
2. Scrape the price of the product
3. Check if the price is below our certain price
4. Send an email if the price is less than our certain price
5. Do this at a certain time everyday


***1. Get the url of the product***

```python
url = input('Enter the Amazon url of the product you want to set this up for: ')
target_price = input('Enter your target price for this item: ')
```

***2. Scrape the price of the product***
```python
import requests

response = requests.get('sample url')

print(response.status_code)
```

**In addition to the URL, when you browser tries to load up a page in Amazon, it also passes a bunch of other information. e.g. Which browser you're using, which computer you have etc.
These additional pieces of information is passed along in the request Headers.
You can see your browser headers by going to this website:
http://myhttpheader.com/**

**You'll need to pass along some headers in order for the request to return the actual website HTML. 
At a minimum you'll need to give your "User-Agent" and "Accept-Language" values in the request header.
If it still does not work try adding more headers.**

Use BeautifulSoup to make soup with the web page HTML you get back. 
You'll need to use the "lxml" parser instead of the "html.parser" for this to work.
If you get an error that says 
"bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: html-parser." 
Then it means you're not using the right parser, 
you'll need to import lxml at the top and install the module then use "lxml" instead of "html.parser" when you make soup.


```python
import requests
import lxml

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Request Line': 'GET / HTTP/1.1',
    'sec-fetch-dest': 'document'
}

response = requests.get(url='https://www.amazon.com/Minoxidil-5-Extra-Strength-Regrowth-Supply/dp/B003U4YC70/ref=sr_1_'
                            '5?crid=1IRGRWFUZVBM3&keywords=minoxidil&qid=1694297437&sprefix=minoxidi%2Caps%2C381&sr=8-5',
                        headers=headers)


print(response.status_code)

soup = BeautifulSoup(response.text, 'lxml')
price = float(soup.find('span', class_='a-price-whole').getText())
print(price)
```

```
200
31.0

Process finished with exit code 0
```

Well, the results are pretty erratic.
Decided to go with this using camelcamelcamel

```python
import requests
from bs4 import BeautifulSoup

url = input('Enter the Amazon url or camel url of the product you want to set this up for: ')
target_price = input('Enter your target price for this item: ')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept-Language': 'en-US,en;q=0.5',
}

response = requests.get(url='https://camelcamelcamel.com/product/B09SWV3BYH?active=summary&tp=1m',
                        headers=headers)

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

price = soup.find(name='span', class_='green')
```

***Note: If using camel, using more headers sometimes does not generate results.
Also there may be some time check. Frequently checking for price returns None***


***3. Check if the price is below our certain price***

```python
def within_budget():
    if price <= float(target_price):
        return True
```

***4. Send an email if the price is less than our certain price***

_4a. Send an email_

```python
import os
import smtplib
import get_price

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
SENDER = EMAIL_ADDRESS
RECEIVER = 'rafi.abdullah.112358@gmail.com'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Price Drop Alert'
    body = f'Your favorite product just got its price slashed. It is now {get_price.price}. ' \
           f'Grab it here -\n{get_price.url}'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(SENDER, RECEIVER, msg)
```

Another, simpler way to send an email would be - 

```python
import os
import smtplib
import get_price
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
SENDER = EMAIL_ADDRESS
RECEIVER = 'rafi.abdullah.112358@gmail.com'

msg = EmailMessage()
msg['Subject'] = 'Price Drop Alert'
msg['From'] = EMAIL_ADDRESS
msg['To'] = RECEIVER
msg.set_content(f'Your favorite product just got its price slashed. It is now {get_price.price}.\n'
                f'Grab it here -\n{get_price.url}')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
```

***5. Do this at a certain time everyday***

```python
import datetime

now = datetime.datetime.now()
print(now)


def is_it_0500():
    if now.hour == 5:
        return True
```

So now you have four files - 

1. main.py
2. get_price.py
3. everyday.py
4. mail_me.py

Main - Scrape and compare from get_price.py. Mail me using mail_me.py. Do this everyday using everyday.py