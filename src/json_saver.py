import json
from abc import ABC, abstractmethod


class Saver(ABC):
    @abstractmethod
    def __init__(self, path):
        pass

    @abstractmethod
    def add_vacancies(self, vacancies):
        pass

    @abstractmethod
    def get_all_vacancies(self):
        pass

    @abstractmethod
    def get_vacancies_by_city(self, city_name):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, min_salary):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass


class JsonSaver(Saver):
    """
    Класс для создания Json файла и чтения данных из файла.
    """

    def __init__(self, path):
        self.path = path

    def add_vacancies(self, vacancies):
        """
        Метод для записи вакансий в json-файл.
        :param vacancies:
        :return:
        """
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)

    def get_all_vacancies(self):
        """
        Метод для открытия и чтения иформации в  json-файле.
        :return:
        """
        with open(self.path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_vacancies_by_city(self, city_name):
        """
        Метод для загрузки вакансий по названию города.
        :param city_name:
        :return:
        """
        all_vacanceis = self.get_all_vacancies()
        corrects = []
        for vacancy in all_vacanceis:
            if vacancy['area'].lower() == city_name.lower():
                corrects.append(vacancy)
        return corrects

    def get_vacancies_by_salary(self, min_salary):
        """
        Метод для загрузки вакансий по зарплате.
        :param min_salary:
        :return:
        """
        all_vacanceis = self.get_all_vacancies()
        corrects = []
        for vacancy in all_vacanceis:
            if vacancy['salary_from'] and vacancy['salary_from'] >= min_salary:
                corrects.append(vacancy)
            elif vacancy['salary_to'] and vacancy['salary_to'] >= min_salary:
                corrects.append(vacancy)

        return corrects

    def delete_vacancies(self):
        """
        Метод для удаления вакансий.
        :return:
        """
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump([], f)

# дописать метод для записи в excel
