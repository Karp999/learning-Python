""" Задача 3 . Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах. """

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


