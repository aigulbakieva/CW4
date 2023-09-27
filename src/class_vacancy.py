class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, title, area, url, salary_from, salary_to, requirement):
        self.title = title
        self.area = area
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement = requirement

    def __str__(self):
        """
        Метод для вывода информации пользователю.
        :return:
        """

        if self.salary_from == 0 and self.salary_to == 0:
            salary_str = "Зарплата: не указана"
        elif self.salary_from and self.salary_to:
            salary_str = f"Зарплата: от {self.salary_from} до {self.salary_to}"
        elif self.salary_from:
            salary_str = f"Зарплата: от {self.salary_from}"
        else:
            salary_str = f"Зарплата: до {self.salary_to}"

        return (f'ВАКАНСИЯ:\n'
                f'======================\n'
                f'Название: {self.title}\n'
                f'Город: {self.area}\n'
                f'{salary_str}\n'
                f'Описание: {self.requirement}\n'
                f'Ссылка: {self.url}\n'
                f'======================\n')

    def __lt__(self, other):
        """
        Метод для сравнения вакансий по зарплате.
        :param other:
        :return:
        """
        other_max = max([other.salary_from, other.salary_to])
        self_max = max([self.salary_from, self.salary_to])
        return self_max < other_max

#   def __gt__(self, other):
#        self.salary > other.salary
