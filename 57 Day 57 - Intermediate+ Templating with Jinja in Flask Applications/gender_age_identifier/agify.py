import requests

# name = 'Teetly'


class age:
    def __init__(self, name):
        self.response = requests.get(f'https://api.agify.io?name={name}')

    def get_age(self):
        data = self.response.json()
        return data['age']
