from abc import ABC, abstractmethod


class Parser(ABC):
    """Класс абстракций, служит в-виде шаблона,
     чтобы не забыть применить методы в парсерах разных сервисов"""
    URL: str
    headers: dict
    params: dict

    @abstractmethod
    def parse(self, data: dict) -> dict:
        """Метод для получения списка словарей необходимых параметров по определенным ключам"""
        pass

    @abstractmethod
    def get_vacations(self) -> dict:
        """Метод для получения списка словарей в формате JSON
        если на стороне сервера неполадки - выводит пустой список"""
        pass
