# Todo 0. Import Modules
import requests
import os
import twilio_module
import send_email

# Todo 1. Pull in the stock price using an API
# Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# stock_api_key = D9TBDRJSOZ5PQBHS
# converted it into environment variable, named STOCK_API
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_url = 'https://www.alphavantage.co/query'

stock_parameters = {
    'function': 'GLOBAL_QUOTE',
    'symbol': STOCK,
    'apikey': os.environ.get('STOCK_API'),
}

# Todo 1a. Find the closing price yesterday and the day before
# Todo 1b. What was the percentage change?

stock_data_response = requests.get(stock_url, params=stock_parameters)
stock_data = stock_data_response.json()
print(stock_data)

# {
# 'Global Quote': {
#     '01. symbol': 'TSLA',
#     '02. open': '258.9200',
#     '03. high': '263.6000',
#     '04. low': '257.2091',
#     '05. price': '260.5400',
#     '06. volume': '167915649',
#     '07. latest trading day': '2023-06-16',
#     '08. previous close': '255.9000',
#     '09. change': '4.6400',
#     '10. change percent': '1.8132%'
#     }
# }

# Todo 2. Find the reason behind the price change
# Todo 2a. Use API to fetch some news
# news api key = d9218e68eeed45d2a9767a0b4c00c9ad
# converted it into environment variable, named NEWS_API
# Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_url = 'https://newsapi.org/v2/everything'

news_parameters = {
    'q': 'Tesla',
    'apiKey': os.environ.get('NEWS_API'),
    'pageSize': 5,
}

news_data_response = requests.get(news_url, params=news_parameters)
news_data = news_data_response.json()
# print(news_data)
# to view fully, click -
# "https://newsapi.org/v2/everything?q=tesla&apiKey=d9218e68eeed45d2a9767a0b4c00c9ad&pageSize=5"
text_message = ''
for i in news_data['articles']:
    text_message += f'Headline: {i["title"]}\n'
    text_message += f'Brief: {i["description"]}\n'
# print(text_message)

# Todo 3. Send yourself an SMS/mail
# used OOP for this one
sms = twilio_module.tw()
sms.send_sms(text_message)
# Additionally I want to make sure I get an email too, so another module named send_email was created
# and this sending mail done with a function
def sm():
    connect = send_email.send_mail()
    connect.send_a_mail(text_message)


change_percent = float(stock_data['Global Quote']['10. change percent'][:-1])
# Todo 4. Optional: Format the SMS message like this: TSLA: 🔺2%
# when sending the mails, smtp was having an issue converting str to ascii, found a little workaround in stackoverflow
if change_percent > 1.00:
    text_message += f'{STOCK}: 🔺{change_percent}%\n'
    text_message = text_message.encode('ascii', 'ignore').decode('ascii')
    sm()
if change_percent < -1.00:
    text_message += f'{STOCK}: 🔻{change_percent}%\n'
    text_message = text_message.encode('ascii', 'ignore').decode('ascii')
    sm()
