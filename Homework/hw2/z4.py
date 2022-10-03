# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

def Multiplication(userNumber):
    commonList = []
    multiply = 1 #первоначальное значение для последующего умножения

    for i in range(userNumber):
        commonList.append(randint(-userNumber, userNumber))
        
    file = open("file.txt", "r")

    for line in file:
        print(line)
        multiply *= commonList[int(line)]

    file.close()

    print(multiply)


print()
userNumber = int(input("Введите число N: "))
print()
print("Произведение равняется:", Multiplication(userNumber) )




