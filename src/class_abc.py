from abc import ABC, abstractmethod


class API(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями.
    """

    @abstractmethod
    def get_vacancies(self, vac_name):
        pass

    @abstractmethod
    def load_all_areas(self):
        pass


