
import json

work_dict = {}
year_list = []

def filewrite(writing):
    with open('book_list_file.json', 'w', encoding='utf-8') as file:
        json.dump(writing, file, indent=4, ensure_ascii=False)
    print('\nГотово👍')

def dictload():
    try:
        global work_dict
        with open('book_list_file.json', 'r', encoding='utf-8') as file:
            work_dict = json.load(file)
    except:
        filewrite({})

while True:
    try:
        print('\nЧто сделать нужно?')
        input_command = input('Добавить/Удалить/Психануть/Найти/Заменить/Посмотреть: ').strip().lower()
        dictload()
        if input_command == 'добавить' or input_command == 'd':
            try:
                name = input('Название книги: ')
                if name in work_dict:
                    print('\nТакая книга есть уже!')
                else:
                    work_dict[name] = int(input('Год выпуска: '))
                    filewrite(work_dict)
            except ValueError:
                print('\nГод выпуска - целое число,\n'
                      'Название - строка!')
        elif input_command == 'удалить' or input_command == 'u':
            input_command = input('Удалить по Номер/Название: ').strip().lower()
            if input_command == 'номер' or input_command == 'no':
                try:
                    del work_dict[list(work_dict.keys())[int(input('Номер книги начиная с нуля: '))]]
                    filewrite(work_dict)
                except ValueError:
                    print('Ты число от строки отличить не можешь балбес?')
                except IndexError:
                    print('\nНет столько книг в списке')
            elif input_command == 'название' or input_command == 'na':
                try:
                    del work_dict[input('Название книги: ')]
                    filewrite(work_dict)
                except KeyError:
                    print('\nТакой книги в списке нет')
            else:
                print('\nНе понял тебя')
        elif input_command == 'психануть' or input_command == 'ps':
            filewrite({})
        elif input_command == 'найти' or input_command == 'n':
            input_command = input('Найти книгу по: Название/Номер/Год: ').strip().lower()
            if input_command == 'название' or input_command == 'na':
                try:
                    input_command = input('Название книги: ')
                    print(f'\nГод издания: {work_dict[input_command]},',
                          f'\nНомер с нуля: {list(work_dict.keys()).index(input_command)}')
                except KeyError:
                    print('\nТакой книги нет в списке')
            elif input_command == 'номер' or input_command == 'no':
                try:
                    input_command = int(input('Номер книги: '))
                    print(f'\nНазвание книги: {list(work_dict.keys())[input_command]}',
                          f'\nГод выпуска: {list(work_dict.values())[input_command]}')
                except ValueError:
                    print('\nНамбер ис интеджер')
                except IndexError:
                    print('\nНет столько книг в списке')
            elif input_command == 'год' or input_command == 'g':
                try:
                    input_command = int(input('Год издания книги: '))
                    for key, value in work_dict.items():
                        if value == input_command:
                            year_list.append(key)
                    if year_list:
                        print('\nНазвание(-я) книг(и):', end=' ')
                        for elem in year_list:
                            print(elem, end=', ')
                    else:
                        print('\nКниг с таким годом нет!\n')
                except ValueError:
                    print('\nНамбер ис интеджер')
            else:
                print('\nНе понял тебя')
        elif input_command == 'заменить' or input_command == 'z':
            try:
                input_command = int(input('Номер книги: '))
                keys = list(work_dict.keys())
                vals = list(work_dict.values())
                keys[input_command] = input('\nНовое название книги:  ')
                vals[input_command] = int(input('\nНовый год (через 2 месяца):  '))
                work_dict.clear()
                for i in range(len(keys)):
                    work_dict[keys[i]] = vals[i]
                filewrite(work_dict)
            except ValueError:
                print('\nНамбер ис интеджер, ворд ис стринг!')
            except IndexError:
                print('\nНет столько книг в списке')
        elif input_command == 'посмотреть' or input_command == 'po':
            print(work_dict)
        else:
            print('\nНе понял тебя')
    except KeyboardInterrupt:
        print('\n\nПрограмма прервана пользователем')
        break
