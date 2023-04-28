from src.requests import HeadHunterAPI, SuperJobAPI


class Vacancy:
    __slots__ = ('title', 'salary_min', 'salary_max', 'employer', 'link')

    def __init__(self, title, salary_min, salary_max, employer, link):
        """Инициализатор класса вакансий"""
        self.title = title
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.employer = employer
        self.link = link

    @staticmethod
    def get_convertation(salary_to, salary_from):
        """Метод для конвертации иностранной валюты в Рубли"""
        salary_min = 0
        salary_max = 0
        if salary_to:
            salary_min = int(salary_to) * 83
        if salary_from:
            salary_max = int(salary_from) * 83
        return salary_min, salary_max


class HHParser(Vacancy):
    """Парсинг вакансий по заданным параметрам для HeadHunter"""

    def get_result(self, data) -> dict:
        pass


class SJOBParser(Vacancy):
    """Парсинг вакансий по заданным параметрам для SuperJob"""

    def get_result(self, data) -> dict:
        pass
