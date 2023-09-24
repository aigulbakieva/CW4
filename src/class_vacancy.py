class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, title, url, salary, requirement):
        self.title = title
        self.url = url
        self.salary = salary
        self.requirement = requirement

    def __str__(self):
        """
        Метод для вывода информации пользователю.
        :return:
        """
        return f'Название: {self.title}, ссылка: {self.url}, зп: {self.salary}, описание: {self.requirement}'

    def __lt__(self, other):
        return self.salary < other.salary

#   def __gt__(self, other):
#        self.salary > other.salary
