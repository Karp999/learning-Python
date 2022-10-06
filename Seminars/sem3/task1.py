""" Задача 1. Реализуйте алгоритм задания случайных чисел 
без использования встроенного генератора псевдослучайных чисел."""
from mimetypes import read_mime_types
from time import time
print()
print(time())
print()

def Func(t):
    return int(str(t).split(".")[1])%100 #функция-разделитель строки

print(Func(time()))
print()