from abc import ABC, abstractmethod


class API(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями.
    """

    @abstractmethod
    def get_vacancies(self, keyword):
        pass

    @abstractmethod
    def formate_vacancies(self, all_vacancies):
        pass
