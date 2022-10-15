""" Задача 3 . Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах. """

from itertools import count


def rle_encode(data):
    encoding = " "
    prev_char = " "
    count = 1

    if not data:
        return " "

    for char in data:
        #если предыдущий и текущий символы не совпадают
        if char != prev_char:
            #то добавляем посчитанное количество символов и сам символ в расшифровку
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            #иначе инкрементируем счетчик, если символы не совпадают
            count += 1
    else:
        #завершение расшифровки
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data):
    decode = " "
    count = " "
    for char in data:
        #если символ - дата
        if char.isdigit():
            # присоединяем его к счетчику
            count += char
        else:
            #иначе, если символ не число, печатаем необходимое количество символов в расшифровку
            decode += char * int(count)
            count = " "
    return decode

decoded_val = rle_decode("5H1L3I6H")
print(decoded_val)
with open("rleDecode.txt", "a") as file:
    file.write(f"{decoded_val}\n")

# with open ("rleEncode.txt", "r") as file:
#     readfile = file.read()
# encoded_val = rle_encode(readfile)
# print(encoded_val)

