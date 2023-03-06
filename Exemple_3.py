"""
сделать локальный чат-бот с хранилищем данных в формате JSON, как объясняли в приложенной записи буткемпа.
"""

import random
import json

def load():
            # загрузить из json
            fname='BD.json' #открываем файл
            with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                BD_local = json.load(fh)  # загружаем из файла данные в словарь data
            print('БД успещно загружена')
            return BD_local

def save():
            # сохранить в json
            with open('BD.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
                fh.write(json.dumps(BD_local, ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
            print('БД успещно сохранена')

BD_local = []

while True:
    command = input("Введите команду")
    if command=="/start":
           print("Бот начал работу")
    elif command=="/stop":
           save()
           print("Бот закончил работу, все файлы сохранены. Хорошего дня :)")
           break
    elif command=="/add":
        