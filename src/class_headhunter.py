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
        self.vac_name = None

    def get_vacancies(self, vac_name):
        self.vac_name = vac_name

        params = {
            'text': {self.vac_name},
            'area': 113,
            'date': 14,
            'per_page': 100
        }

        response = requests.get(self.HH_API_URL, params=params)
        # response_data = json.load(response.text)
        return response.json()

    def add_vacancy(self):
        vacancy_list = []
        hh_api = HeadHunter()
        hh_vacancies = hh_api.get_vacancies(self.vac_name)
        # return response.json()['items']
        for item in hh_vacancies['items']:
            salary = item['salary']
            if salary is None:
                vacancy_list.append({
                    'title': item['name'],
                    'url': 'https://hh.ru/vacancy/' + item['id'],
                    'salary_from': 0,
                    'salary_to': 0,
                    'requirement': item['snippet']['requirement']
                })

            elif salary['from'] is None:
                vacancy_list.append({
                    'title': item['name'],
                    'url': 'https://hh.ru/vacancy/' + item['id'],
                    'salary_from': 0,
                    'salary_to': salary['to'],
                    'requirement': item['snippet']['requirement']
                })

            elif salary['to'] is None:
                vacancy_list.append({
                    'title': item['name'],
                    'url': 'https://hh.ru/vacancy/' + item['id'],
                    'salary_from': salary['from'],
                    'salary_to': 0,
                    'requirement': item['snippet']['requirement']
                })

            else:
                vacancy_list.append({
                    'title': item['name'],
                    'url': 'https://hh.ru/vacancy/' + item['id'],
                    'salary': salary['from'],
                    'requirement': item['snippet']['requirement']
                })

        return vacancy_list

    def load_all_areas(self):
        response = requests.get(self.HH_API_URL_AREAS)
        return response.json()
