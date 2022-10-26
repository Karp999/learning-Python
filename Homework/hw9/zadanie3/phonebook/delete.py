import re
import logger

def delete():
    with open ('Phonebook_string.csv', 'r', encoding='utf-8', newline='') as file:
        lst = file.readlines()
        surname = input('Введите фамилию: ')
        pattern = re.compile(re.escape(surname))
        with open('Phonebook_string.csv', 'w', encoding='utf-8', newline='') as f:
            for i in lst:
                result = pattern.search(i)
                if result is None:
                    f.write(i)
    logger.info_logger(f'Удаление записи: {pattern}')
