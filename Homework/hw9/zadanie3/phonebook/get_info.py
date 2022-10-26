def get_info ():
    info = []
    surname = input('Введите фамилию: ')
    info.append(surname)
    name = input('Введите имя: ')
    info.append(name)
    phone_number = input('Введите номер телефона: ')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info