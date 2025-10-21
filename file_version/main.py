
import json

work_dict = {}
closer_work_dict = {}

while True:
    with open('book_list_file.json', 'r+', encoding='utf-8') as file:
        print('Что сделать нужно?')
        input_command = input('Добавить/Удалить/Психануть/Поиск: ').strip().lower()
        if input_command == 'добавить' or input_command == 'd':
            try:
                closer_work_dict = json.load(file)
            except: pass
            finally:
                work_dict[input('Название книги: ')] = {'date': int(input('Год выпуска: ')),
                                                        'id': len(closer_work_dict)}
                closer_work_dict.update(work_dict)
                try:
                    with open('book_list_file.json', 'w', encoding='utf-8') as file:
                        json.dump(closer_work_dict, file, indent=4, ensure_ascii=False)
                except: pass
                finally:
                    print(work_dict)
                    print(closer_work_dict)
        elif input_command == 'удалить' or input_command == 'u':
            print('Удалить по номеру или по названию?')
            input_command = input('Номер/Название: ').strip().lower()
            if input_command == 'номер' or input_command == 'no':
                input_command = int(input('Номер книги, отсчет с нуля: '))
                try:
                    closer_work_dict = json.load(file)
                except: pass
                finally:
                    for i in range(len(closer_work_dict - 1)):
                        if closer_work_dict[i]['id'] == input_command:
                            del closer_work_dict[i]
                            try:
                                with open('book_list_file.json', 'w', encoding = 'utf-8') as file:
                                    json.dump(closer_work_dict, file, indent = 4, ensure_ascii = False)
                            except:
                                pass
                            finally:
                                print('Готово!')
            elif input_command == 'название' or input_command == 'na':
                try:
                    closer_work_dict = json.load(file)
                except: pass
                finally:
                    del closer_work_dict[input('Название книги: ')]
                    try:
                        with open('book_list_file.json', 'w', encoding = 'utf-8') as file:
                            json.dump(closer_work_dict, file, indent = 4, ensure_ascii = False)
                    except:
                        pass
                    finally:
                        print('Готово!')

            else:
                print('Не понял тебя')
        elif input_command == 'психануть' or input_command == 'ps':
            try:
                with open('book_list_file.json', 'w', encoding = 'utf-8') as file:
                    json.dump(file)
            except:
                pass
            finally:
                print('Весь список очищен. Добавь новые книги - читать полезно')
        else:
            print('Не понял тебя')
