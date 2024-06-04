import requests
from config import BASE_URL

class APIClient:

    @staticmethod
    def get(endpoint):
        url = f'{BASE_URL}{endpoint}'
        response = requests.get(url)
        return response
