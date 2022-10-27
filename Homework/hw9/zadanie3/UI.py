import search
import write_read
import delete

def menu():
    m = input('''Поиск контакта в телефонной книге 1 (строка): введите 1.
             \nПоиск контакта в телефонной книге 2 (столбец): введите 2
             \nУдалить контакт: введите 3. 
             \nСоздать новую запись, сохранить в телефонной книге 1 (строка): введите 4. 
             \nСоздать новую запись, сохранить в в телефонной книге 2 (столбец): введите 5. 
             \nВыход: введите 0.\n''')

    match m:
        case '1':
            return search.search_string()
        case '2':
            return search.search_column()
        case '3':
            return delete.delete()    
        case '4':
            return write_read.write_file_string()
        case '5':
            return write_read.write_file_column()
        case '0':
            return