""" Задача 3. Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.    
Пример:    
[1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
import random

print()
sizeList = int(input("Задайте размер списка: "))
initialList  = []
for i in range(sizeList):
    initialList.append(round(random.uniform(1,9),2))
print(initialList)
print()

def MaxMinSubtraction(initialList):
    # задаю первоначальные максимальное и минимальное значения (начну с 0 позиции, а потом буду перебирать список)
    max = round(initialList[0] % 1,2)
    min = round(initialList[0] % 1,2)
    
    for i in range(len(initialList)):
        if initialList[i] % 1 > max:
            max = round(initialList[i] % 1, 2)
        if initialList[i] % 1 > 0 and initialList[i] % 1 < min:
            min = round(initialList[i] % 1, 2)
    print ("Максимальная дробная часть: ", max)
    print ("Минимальная дробная часть: ", min)
    print()
    subtraction = round(max-min,2)
    return subtraction
    
print ("Разница между максимальной и минимальной дробной частью элементов равна: ", MaxMinSubtraction(initialList))
print()


