import requests
from datetime import datetime
from nutrition import Nutritionx
nutrition = Nutritionx()

class Sheet:
    def __init__(self):
        self.sheet = open('keys/sheet.txt', 'r').read()
        token = open('keys/sheety_token.txt', 'r').read()
        exercise, calories, duration = nutrition.exercise()

        self.header = {
            'Authorization': token
        }

        self.param = {
            'exerc': {
                'date': datetime.now().strftime('%Y-%m-%d'),
                'time': datetime.now().strftime("%H:%M:%S"),
                'exercise': exercise,
                "duration": duration,
                "calories": calories
            }
        }

    def add_row(self):
        response = requests.post(url=self.sheet, json=self.param, headers=self.header)