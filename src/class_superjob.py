import requests
import os
from src.class_abc import API


class SuperJob(API):
    """
    Класс для работы с сайтом SuperJob через API.
    """
    SJ_API_URL = 'https://api.superjob.ru/2.0/vacancies'
    SJ_API_URL_AREAS = 'https://api.superjob.ru/2.0/towns/'
    SJ_TOKEN = os.getenv('SJ_TOKEN')

    def __init__(self):
        self.vac_name = None

    def get_vacancies(self, keyword):
        """
        Метод для получения всех вакансий на платформе SJ по API.
        :param keyword:
        :return:
        """
        headers = {
            'X-Api-App-Id': self.SJ_TOKEN
        }
        params = {
            'keyword': keyword,
            'count': 100
        }
        response = requests.get(self.SJ_API_URL, headers=headers, params=params)
        return response.json()

    def formate_vacancies(self, all_vacancies):
        """
        Метод для получения информации о вакансиях по заданным параметрам.
        :param all_vacancies:
        :return:
        """
        vacancy_list = []
        for item in all_vacancies['objects']:
            result = {
                'title': item['profession'],
                'area': item['town']['title'],
                'url': item['link'],
                'salary_from': item['payment_from'],
                'salary_to': item['payment_to'],
                'requirement': item['candidat']
            }
            vacancy_list.append(result)
        return vacancy_list

    def load_all_areas(self):
        response = requests.get(self.SJ_API_URL_AREAS)
        return response.json()
