from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup(response.text, 'html.parser')

movies_dict = {}
for i in soup.select(selector='.listicleItem_listicle-item__title__hW_Kn'):
    temp_list = i.getText().split(') ')
    movies_dict[int(temp_list[0])] = temp_list[1]

movies_dict_sorted = dict(sorted(movies_dict.items()))

movies_list = [i.getText() for i in soup.select(selector='.listicleItem_listicle-item__title__hW_Kn')]
print(movies_list[::-1])

# for i,j in movies_dict_sorted.items():
#     print(f'{i}) {j}')

with open('100_movies.txt', mode='w') as file:
    for i,j in movies_dict_sorted.items():
            file.write(f'{i}) {j} \n')