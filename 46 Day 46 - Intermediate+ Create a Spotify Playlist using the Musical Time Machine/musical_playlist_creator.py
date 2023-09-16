import requests
from bs4 import BeautifulSoup


client_id = '41a2a7c4cbfc40598838afb53126caf5'
client_secret = '16353ab03aba4b28a947536d49e93d83'
redirect_uri = 'http://localhost:3000'

year = input("What day do you want to travel back to? (yyyy-mm-dd) - ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/2020-01-01/")
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.findAll(name="h3", class_="a-no-trucate"))
# print(soup.findAll(name="span", class_="a-no-trucate"))
song_titles = []
singer_names = []
for i in soup.select(selector='li ul li h3'):
    song_titles.append(i.getText().strip())


