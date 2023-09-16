from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
# print(response.status_code)

# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# print(soup.title)


# for i in soup.select('.titleline'):
    # print(i.getText())

# for j in soup.find_all(name='span', class_='titleline'):
#     print(j.getText())
#     print(j.get('a'))

# for k in soup.select(selector='.titleline a'):
#     if k.get('href').startswith('https'):
#         print(k.get('href'))
#
# for l in soup.select(selector= '.score'):
#     print(int(l.getText()[:-7]))

title_list = [i.getText() for i in soup.select(selector='.titleline')]
link_list = [k.get('href') for k in soup.select(selector='.titleline a') if k.get('href').startswith('https')]
score_list = [int(l.getText()[:-7]) for l in soup.select(selector= '.score')]

print(title_list)
print(score_list)

print(sorted(score_list, reverse=True))

print(score_list.index(sorted(score_list, reverse=True)[0]))

for i in sorted(score_list, reverse=True)[0:10]:
    index_num = score_list.index(i)
    print(title_list[index_num])
    print(link_list[index_num])
