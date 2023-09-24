import json


class JsonSaver:
    """
    Класс для создания Json файла и чтения данных из файла.
    """

    def __init__(self):
        self.file_path = 'file1.json'

    def add_vacancy(self, job_data):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json_file = json.dumps(job_data, indent=4, ensure_ascii=False)
            f.write(json_file)

    def get_vacancy(self, option):
        fav_vacancy = []
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for i in data:
            if option in i['title']:
                fav_vacancy.append(i)
        return fav_vacancy



    def delete_vacancy(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write("")
