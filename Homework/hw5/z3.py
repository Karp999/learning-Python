""" Задача 3 . Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах. """

print()
encTXT = input("Введите имя файла для сжатия данных: ")
decTXT = input("Введите имя файла для восстановления данных: ")

def ReadingFiles(file):
    data = open(file, "r")
    for line in data:
        print(line)
    data.close()

print(ReadingFiles(encTXT))
print(ReadingFiles(decTXT))


