import os

import requests
from dotenv import load_dotenv

from service.abstract import Parser
from settings import ENV_FILE

load_dotenv(ENV_FILE)


# В данном классе необходим header, так как 'SJob' работает на защищенных протоколах.

class SJParser(Parser):
    """Класс для сбора и систематизации определенной информации на сайте SuperJob"""
    api_key: str = os.getenv('SECRET_KEY')
    URL = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': api_key
    }
    params = {
        "keyword": "Python"
    }

    def parse(self, data: dict) -> list[dict]:
        """Метод для получения списка словарей необходимых параметров по определенным ключам"""
        answer = []
        for el in data['objects']:
            answer.append({
                'title': el['profession'],
                'salary_max': el['payment_to'],
                'salary_min': el['payment_from'],
                'employer': el['firm_name'],
                'link': el['link'],
                'source': 'Super Job'
            }
            )
        return answer

    def get_vacations(self) -> list[dict]:
        """Метод для получения списка словарей в формате JSON
        если на стороне сервера неполадки - выводит пустой список"""
        response = requests.get(self.URL, headers=self.headers, params=self.params)
        if response.status_code == 200:
            return self.parse(response.json())
        return []
