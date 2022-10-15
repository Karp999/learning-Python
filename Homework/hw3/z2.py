""" Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.    
Пример:    
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
"""
from random import randint

print()
sizeList = int(input("Задайте размер списка: "))
initialList  = []
for i in range(sizeList):
    initialList.append(randint(1, 9))
print(initialList)
print()

def Multiplication(initialList):
    resultList = []
    for i in range(len(initialList)):
        if i <= len(initialList)-1-i:
            resultList.append(initialList[i]*initialList[len(initialList)-1-i])
            print("Промежуточный результат:", resultList) # проверка 
    print()
    return resultList

print ("Произведение пар чисел списка:", Multiplication(initialList))
print()

