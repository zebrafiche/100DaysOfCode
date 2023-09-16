from bs4 import BeautifulSoup

with open(r'website.html', encoding="utf8") as website:
    contents = website.read()
    print(contents)


soup = BeautifulSoup(contents, 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup)

print(soup.prettify())

print(soup.a)
print(soup.p)


print(soup.find_all("a"))
print(soup.find_all("p"))

anchor_tags = soup.find_all("a")
for i in anchor_tags:
    print(i.getText())

p_tags = soup.find_all("a")
for j in p_tags:
    print(j.get('href'))

soup.find(name='h1', id='name')

soup.find(name='h3', class_='heading')
soup.find_all(name='h3', class_='heading')

soup.select_one(selector='p em')
soup.select_one(selector='p a')
print(soup.select_one(selector='p a').getText())

soup.select_one('#name')
soup.select_one('.heading')
soup.select('.heading')
print(soup.select(selector='body a'))
