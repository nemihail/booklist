
book_list = []

def check(finding):
    for elem in book_list:
        if finding = elem.lower():
            return True
        else:
            pass

while True:
    print()
    for elem in book_list:
        print(elem)

    print('\nЧто сделать нужно с книгой?')
    input_command = input('Добавить/Удалить/Индекс/Психануть: ')
    if input_command.lower() == 'добавить':
        book_list.append(input('Введи название книги: '))
    elif input_command.lower() == 'удалить':
        input_command = input('Введи название книги: ').lower()
        if check(input_command) == True:
            book_list.remove(input_command)
        else:
            print('Такой книги не найдено')
    elif input_command.lower() == 'индекс':
        input_command == int(input('Введи индекс: '))
        if input_command < len(book_list):
            if check(book_list[input_command]) == True:
                print(book_list[input_command])
            else:
                print('Такой книги не найдено')
        else:
            print('В списке нет столько книг!')
            
    elif input_command.lower() == 'психануть':
        if input('Точно? Да/Нет: ').lower() == 'да':
              book_list.clear()
        elif input('Точно? Да/Нет: ').lower() == 'нет':
              print('Правильно, читать полезно')
        else:
              print('Не понял тебя')
    else:
        print('Не понял тебя')
        