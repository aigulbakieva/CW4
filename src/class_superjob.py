import requests
from src.class_abc import API


class SuperJob(API):
    SJ_API_URL = 'https://api.superjob.ru/2.0/vacancies'
    SJ_API_URL_AREAS = 'https://api.superjob.ru/2.0/towns/'
    SJ_TOKEN = "v3.r.137841891.a2380955865d5e17875cca2dae4a93b861ddc79c.24df6bd943c397f563c40253463e3090ff3c54b7"

    def __init__(self):
        self.vac_name = None

    def get_vacancies(self, vac_name):
        self.vac_name = vac_name
        headers = {
            'X-Api-App-Id': self.SJ_TOKEN
        }
        params = {
            'keyword': vac_name,
            'town': 1,
            'period': 1,
            'count': 100
        }
        response = requests.get(self.SJ_API_URL, headers=headers, params=params)
        return response.json()

    def add_vacancy(self):
        vacancy_list = []
        sj_api = SuperJob()
        sj_vacancies = sj_api.get_vacancies(self.vac_name)
        for item in sj_vacancies['objects']:
            salary_from = item['payment_from']
            salary_to = item['payment_to']

            if salary_from == 0 and salary_to == 0:
                vacancy_list.append({
                    "title": item['profession'],
                    "url": item['link'],
                    "salary_from": 0,
                    "salary_to": 0,
                    "requirement": item['candidat']
                })

            elif salary_from == 0:
                vacancy_list.append({
                    "title": item['profession'],
                    "url": item['link'],
                    "salary_from": 0,
                    "salary_to": item['payment_to'],
                    "requirement": item['candidat']
                })

            elif salary_to == 0:
                vacancy_list.append({
                    "title": item['profession'],
                    "url": item['link'],
                    "salary_from": item['payment_from'],
                    "salary_to": 0,
                    "requirement": item['candidat']
                })

            else:
                vacancy_list.append({
                    "title": item['profession'],
                    "url": item['link'],
                    "salary_from": item['payment_from'],
                    "salary_to": ['payment_to'],
                    "requirement": item['candidat']
                })
        return vacancy_list

    def load_all_areas(self):
        response = requests.get(self.SJ_API_URL_AREAS)
        return response.json()
