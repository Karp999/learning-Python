""" Задача 1. Задайте список из нескольких чисел. 
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.    
Пример:    
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""
# ДО: 
# from random import randint

# print()
# sizeList = int(input("Задайте размер списка: "))
# initialList  = []
# for i in range(sizeList):
#     initialList.append(randint(1, 10))
# print(initialList)
# print()

# def SumOddNums(sizeList, initialList):
#     sum = 0
#     for i in range(sizeList):
#         if i % 2 != 0:
#             sum += int(initialList[i])
#             print("Промежуточная сумма:",sum) # для проверки
#     print()
#     return sum

# print("Сумма элементов списка на нечётных позициях:", SumOddNums(sizeList, initialList))
# print()

# ПОСЛЕ:
from random import randint
sizeList = int(input("Задайте размер списка: "))
initialList  = [randint(1, 10) for i in range(sizeList)] # List Comprehension
print(initialList)
oddNums = [ initialList[i] for i in range (sizeList) if i % 2 == 1 ] # List Comprehension
print(oddNums) 
sumOddNums = 0 
for i in range (len(oddNums)): #хотела сумму расписать(пример ниже), пробовала по разному,
# но выскакивает ошибка: TypeError: can only concatenate list (not "int") to list, поэтому использую for
    sumOddNums += int(oddNums[i])
print("Сумма элементов списка на нечётных позициях:", sumOddNums)

# from random import randint
# print()
# sizeList = int(input("Задайте размер списка: "))
# initialList  = [randint(1, 10) for i in range(sizeList)] 
# print(initialList)
# print()
"""попытка сделать через filter() и lambda, но выдает нечетные элементы,а не их позиции"""
# oddNums = list(filter(lambda i: i % 2 != 0 , initialList)) 
# sumOddNums = [(int(oddNums[i])) for i in range (len(int(oddNums+1))) (int(oddNums[i])) + (int(oddNums[i]))]
# print("Сумма элементов списка на нечётных позициях:", sumOddNums)

