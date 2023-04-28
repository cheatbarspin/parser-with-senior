import os
from abc import ABC, abstractmethod
import requests
from settings import ENV_FILE
from dotenv import load_dotenv

load_dotenv(ENV_FILE)


class Engine(ABC):

    @abstractmethod
    def get_request(self):
        """Метод для получения запроса от API"""
        pass


class HeadHunterAPI(Engine):
    """Класс для получения запроса от API - HeadHunter"""

    def get_request(self):
        pass


class SuperJobAPI(Engine):
    """Класс получения запроса от API - SuperJob"""

    api_key: str = os.getenv('SECRET_KEY')

    def get_request(self):
        pass
