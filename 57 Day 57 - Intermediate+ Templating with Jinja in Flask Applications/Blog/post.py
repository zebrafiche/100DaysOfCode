import requests


class Post:
    def __init__(self):
        self.response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')

    def get_posts(self):
        data = self.response.json()
        return data

# response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
# print(response.status_code)
# data = response.json()
# for i in data:
#     print(i["title"])
#     print(i["subtitle"])
#     print(i["id"])
#     print(i["body"])
