import json

from parsers.hh_parser import HHParser
from parsers.sj_parser import SJParser
from src.vacancy.hh_vacancy import HeadHunterVacancy
from src.vacancy.sj_vacancy import SuperJobVacancy


class Service:
    list_sj: list[SuperJobVacancy] = []
    list_hh: list[HeadHunterVacancy] = []

    def update_from_site(self):
        """Метод получения информации и записи в список"""
        parser_sj = SJParser()
        for el in parser_sj.get_vacations():
            self.list_sj.append(SuperJobVacancy(
                title=el['title'],
                salary_max=el['salary_max'],
                salary_min=el['salary_min'],
                employer=el['employer'],
                link=el['link'],
                source=el['source'],
            ))
        parser_hh = HHParser()
        for el in parser_hh.get_vacations():
            self.list_hh.append(HeadHunterVacancy(
                title=el['title'],
                salary_max=el['salary_max'],
                salary_min=el['salary_min'],
                employer=el['employer'],
                link=el['link'],
                source=el['source'],
            ))

    def read_from_file(self, filename: str = 'db.json'):
        """Метод для чтения файла с возможностью получения информации из вакансий"""
        with open(filename, 'r') as f:
            raw_data = f.read()
            data = json.loads(raw_data)
            for el in data:
                if el['source'] == "Super Job":
                    self.list_sj.append(SuperJobVacancy(
                        title=el['title'],
                        salary_max=el['salary_max'],
                        salary_min=el['salary_min'],
                        employer=el['employer'],
                        link=el['link'],
                        source=el['source'],
                    ))
                else:
                    self.list_hh.append(HeadHunterVacancy(
                        title=el['title'],
                        salary_max=el['salary_max'],
                        salary_min=el['salary_min'],
                        employer=el['employer'],
                        link=el['link'],
                        source=el['source'],
                    ))

    def write_to_file(self, filename: str = 'db.json'):
        """Метод записи в файл найденных вакансий"""
        with open(filename, 'w') as f:
            data = self.list_sj + self.list_hh
            data_dict = []
            for el in data:
                data_dict.append(el.to_dict())
            f.write(json.dumps(data_dict, indent=4, ensure_ascii=False))

    # def find_by_name(self, vacation_name: str):
    #     """Метод поиска данных по названию, например: по названию профессии"""
    #     with open('db.json', 'r') as f:
    #         raw_data = f.read()
    #         data = json.loads(raw_data)
    #         research = []
    #         for el in data:
    #             if el['title'] in vacation_name:
    #                 research.append(el)
    #                 print(research)
    #
    # def find_by_salary(self, salary: int):
    #     """Метод поиска данных по зарплате"""
    #     with open('db.json', 'r') as f:
    #         raw_data = f.read()
    #         data = json.loads(raw_data)
    #         research = []
    #         for el in data:
    #             if el['salary_min'] <= salary:
    #                 research.append(el)
    #         print(research)


s = Service()
# s.read_from_file()
# s.find_by_salary(100000)
# for el in s.list_sj:
    # print(el.title)
s.update_from_site()
# for el in s.list_sj:
#     print(el)
s.write_to_file()
# ss = SuperJobVacancy()




