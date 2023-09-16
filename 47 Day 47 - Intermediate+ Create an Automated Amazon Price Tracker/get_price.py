import requests
from bs4 import BeautifulSoup
import lxml

# url = input('Enter the Amazon url or camel url of the product you want to set this up for: ')
# target_price = input('Enter your target price for this item: ')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Request Line': 'GET / HTTP/1.1',
    'sec-fetch-dest': 'document'
}

price = 0


def scrape(url):
    response = requests.get(url=url,
                            headers=headers)

    print(response.status_code)

    soup = BeautifulSoup(response.text, 'lxml')
    global price
    price = soup.find(name='span', class_='aok-offscreen')
    print(price)


def within_budget(item_price):
    if float(price) <= float(item_price):
        return True
