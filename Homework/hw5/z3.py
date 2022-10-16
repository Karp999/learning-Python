""" Задача 3 . Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах. """

#!!! ошибка FileNotFoundError: [Errno 2] No such file or directory: 'enc.txt', хотя файл на месте

print()
encTXT = "enc.txt"
decTXT = "dec.txt"

def ReadingFiles(file):
    data = open(file, "r")
    for line in data:
        print(line)
    data.close()

print(ReadingFiles(encTXT))
print(ReadingFiles(decTXT))

# Описание сжатия данных
def Encryption(encTXT):
    encoding = " "
    prev_char = " "
    count = 1

    if not encTXT:
        return " "

    for char in encTXT:
        if char != prev_char: # сравниваются текущий и предыдущий символы, при их несовпадении 
            # посчитанное количество символов и сам символ добавляются в расшифровку
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else: 
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


# Описание восстановления данных
def Decoding (decTXT):
    decode = " "
    count = " "
    for char in decTXT:
        if char.isdigit(): # если символ - дата, присоединяем его к счетчику
            count += char
        else: # иначе печатаем количество символов в расшифровку
            decode += char * int(count)
            count = " "
    return decode

Encryption(decTXT)
Decoding(encTXT)



