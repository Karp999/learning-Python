""" Задача 1. Задайте список из нескольких чисел. 
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.    
Пример:    
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""
from random import randint

print()
sizeList = int(input("Задайте размер списка: "))
initialList  = []
for i in range(sizeList):
    initialList.append(randint(1, 10))
print(initialList)
print()

def SumOddNums(sizeList, initialList):
    sum = 0
    for i in range(sizeList):
        if i % 2 != 0:
            sum += int(initialList[i])
            print("Промежуточная сумма:",sum) # для проверки
    print()
    return sum

print("Сумма элементов списка на нечётных позициях:", SumOddNums(sizeList, initialList))
print()