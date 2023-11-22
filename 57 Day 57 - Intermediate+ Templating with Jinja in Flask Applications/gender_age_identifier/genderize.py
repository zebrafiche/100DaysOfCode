import requests

# name = 'Rafi'


class gender:
    def __init__(self, name):
        self.response = requests.get(f'https://api.genderize.io?name={name}')

    def get_gender(self):
        data = self.response.json()
        return data['gender']
