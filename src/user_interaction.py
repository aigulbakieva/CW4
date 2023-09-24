from src.class_headhunter import HeadHunter
from src.class_superjob import SuperJob
from class_vacancy import Vacancy
from json_saver import JsonSaver


def user_interaction():
    """
    Функция взаимодействия с пользователем через консоль.
    :return:
    """
    hh_api = HeadHunter()
    superjob_api = SuperJob()
    json_saver = JsonSaver()
    while True:
        platforms = input("Выберите платформу для поиска вакансий:\n"
                          "1.HeadHunter\n"
                          "2.SuperJob\n"
                          "3.HeadHunter + SuperJob\n"
                          "4.Завершить поиск\n")

