import os
from src.class_headhunter import HeadHunter
from src.class_superjob import SuperJob
from class_vacancy import Vacancy
from json_saver import JsonSaver
from config import ROOT_DIR


def user_interaction():
    """
    Функция взаимодействия с пользователем через консоль.
    :return:
    """
    while True:
        answer = input("Выберите платформу для поиска вакансий:\n"
                       "1.HeadHunter\n"
                       "2.SuperJob\n"
                       "3.HeadHunter + SuperJob\n"
                       "4.Завершить поиск\n")

        platforms = []
        if answer == '1':
            platforms.append(HeadHunter())
        elif answer == '2':
            platforms.append(SuperJob())
        elif answer == '3':
            platforms.append(HeadHunter())
            platforms.append(SuperJob())
        else:
            print("Всего доброго")
            break

        answer = input("Введите запрос для поиска вакансий")
        formated_vacancies_data = []
        for platform in platforms:
            all_vacancies = platform.get_vacancies(answer)
            formated_vacancies_data.extend(platform.formate_vacancies(all_vacancies))

        if len(formated_vacancies_data) == 0:
            print("Вакансий не найдено")
            break

        filename = 'vacancies.json'
        file_path = os.path.join(ROOT_DIR, 'data', filename)
        json_saver = JsonSaver(file_path)
        json_saver.add_vacancies(formated_vacancies_data)

        print(f"Все найденные вакансии сохранены в файл {file_path}\n"
              f"1. Найти по городу\n"
              f"2. Найти по минимальной зарплате\n"
              f"3. Вывести топ N вакансий по зарплате\n"
              f"4. Вывести все вакансии\n"
              f"5. Завершить программу")
        answer = input()
        if answer == '1':
            city_name = input("Введите название города:\n").lower().strip()
            vacancies = json_saver.get_vacancies_by_city(city_name)
        elif answer == '2':
            min_salary = int(input("Введите минимальную зарплату:\n").strip())
            vacancies = json_saver.get_vacancies_by_salary(min_salary)
        elif answer == '3':
            top_n = int(input("Сколько топ-вакансий вывести:\n").strip())
            vacancies = json_saver.get_all_vacancies()
        elif answer == '4':
            vacancies = json_saver.get_all_vacancies()
        else:
            print("Всего доброго")
            break

        vacancy_instances = [Vacancy(**vacancy) for vacancy in vacancies]

        if answer == '3':
            sorted_vacancies = sorted(vacancy_instances, reverse=True)
            if len(sorted_vacancies) < top_n:
                vacancy_instances = sorted_vacancies
            else:
                vacancy_instances = sorted_vacancies[:top_n]

        for vacancy_instance in vacancy_instances:
            print(vacancy_instance)
            print()

        print("Введите yes для повторного использования")
        answer = input()
        if not answer == 'yes':
            print("Всего доброго")
            break
