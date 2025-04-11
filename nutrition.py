import requests


class Nutritionx:
    def __init__(self):
        app_key = open('keys/app-key.txt', 'r').read()
        app_id = open('keys/app-id.txt', 'r').read()
        self.header = {
            'x-app-id': app_id,
            'x-app-key': app_key
        }

    def exercise(self):
        nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
        question = str(input("Tell what exercise you did: "))
        exercise = {
            'query': question
        }
        response = requests.post(url=nutritionix_endpoint, headers=self.header, json=exercise).json()
        response = response['exercises'][0]
        return response['name'], response['nf_calories'], response['duration_min']
