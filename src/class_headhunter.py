import requests
from src.class_abc import API


class HeadHunter(API):
    """
    Класс для работы с сайтом headhunter через API
    """

    HH_API_URL = 'https://api.hh.ru/vacancies'
    HH_API_URL_AREAS = 'https://api.hh.ru/areas'
    HH_AREAS_JSON = 'data/areas/headhunter_areas.json'

    def __init__(self):
        pass

    def get_vacancies(self, keyword):
        """
        Метод для получения всех вакансий на платформе HH по API.
        :param keyword:
        :return:
        """
        params = {
            'text': keyword,
            'per_page': 100
        }

        response = requests.get(self.HH_API_URL, params=params)
        # response_data = json.load(response.text)
        return response.json()

    def formate_vacancies(self, all_vacancies):
        """
        Метод для получения информации о вакансиях по заданным параметрам.
        :param all_vacancies:
        :return:
        """
        vacancy_list = []
        for item in all_vacancies['items']:
            salary = item['salary']
            result = {
                'title': item['name'],
                'area': item['area']['name'],
                'url': 'https://hh.ru/vacancy/' + item['id'],
                'salary_from': 0 if salary is None or salary['from'] is None else salary['from'],
                'salary_to': 0 if salary is None or salary['to'] is None else salary['to'],
                'requirement': item['snippet']['requirement']
            }
            vacancy_list.append(result)
        return vacancy_list
