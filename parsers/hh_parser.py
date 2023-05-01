import requests
from service.abstract import Parser


class HHParser(Parser):
    URL = 'https://api.hh.ru/vacancies'
    # headers = {
    #     "User-Agent": "MyApp/1.0 (my-app-feedback@example.com)"
    # }
    params = {
        "text": "Python"
    }

    def parse(self, data: dict) -> list[dict]:
        answer = []
        for el in data['items']:
            salary = el.get('salary')
            if salary:
                answer.append({
                    "title": el['name'],
                    "employer": el['employer']['name'],
                    "salary_max": el['salary']['to'],
                    "salary_min": el['salary']['from'],
                    "link": el['alternate_url'],
                    "source": 'HeadHunter'
                }
                )
        return answer

    def get_vacations(self) -> list[dict]:
        response = requests.get(self.URL, params=self.params)
        if response.status_code == 200:
            return self.parse(response.json())
        return []

#
# hh = HHParser()
# print(hh.get_vacations())
