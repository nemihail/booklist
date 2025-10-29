
import json

work_dict = {}

def filewrite():
    with open('book_list_file.json', 'w', encoding='utf-8') as file:
        json.dump(work_dict, file, indent=4, ensure_ascii=False)

def dictload():
    global work_dict
    with open('book_list_file.json', 'r', encoding='utf-8') as file:
        work_dict = json.load(file)

while True:
    print('Что сделать нужно?')
    input_command = input('Добавить/Удалить/Психануть/Поиск: ').strip().lower()
    if input_command == 'добавить' or input_command == 'd':                             # добавление книги в список
        dictload()
        work_dict[input('Название книги: ')] = int(input('Год выпуска: '))
        filewrite()
        print(work_dict)
    else:                                                                               # если опечатка
        print('Не понял тебя')
