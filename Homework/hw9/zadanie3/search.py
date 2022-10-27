import write_read

def search_string():
    surname = input('Введите фамилию: ')
    file = write_read.read_file_string()
    new_file = file.split()
    if surname in new_file:
        for i in range(len(new_file)):
            if surname == new_file[i]:
                print(new_file [i], new_file[i+1], new_file[i+2], new_file[i+3])
    else:
       print('Контакт не найден') 

def search_column():
    surname = input('Введите фамилию: ')
    file = write_read.read_file_column()
    new_file = file.split()
    if surname in new_file:
        for i in range(len(new_file)):
            if surname == new_file[i]:
                print(f'{new_file [i]}\n{new_file[i+1]}\n{new_file[i+2]}\n{new_file[i+3]}')
    else:
       print('Контакт не найден') 