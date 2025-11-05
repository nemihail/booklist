
# крайне устаревшая версия!! только для ознакомлениЯ

book_list = []

while True:
    print()
    for elem, i in zip(book_list, range(len(book_list))):
        print(i, '. ', elem)
    print('\nЧто сделать со списком?')
    input_command = input('Добавить/Удалить/Индекс/Психануть: ')
    if input_command.strip().lower() == 'добавить':
        input_command = input('Введи имя книги: ')
        book_list.append(input_command)
    elif input_command.strip().lower() == 'удалить':
        input_command = int(input('Введите индекс книги: '))
        if input_command < len(book_list):
            book_list.pop(input_command)
        else:
            print('\nНет столько книг!')
    elif input_command.strip().lower() == 'индекс':
        input_command = int(input('Введите индекс книги: '))
        if input_command < len(book_list):
            print('\n', book_list[input_command])
        else:
            print('\nНет столько книг!')
    elif input_command.strip().lower() == 'психануть':
        book_list.clear()
    else:
        print('\nНе поняи тебя')
    
