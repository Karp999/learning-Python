# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

print()
userNumber = int(input("Введите число N: "))

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
print("Произведение равняется:", Multiplication(userNumber) )

# в этой задаче был ступор, семинар помог подразобраться. Однако, у меня выскакивает ошибка 
# FileNotFoundError: [Errno 2] No such file or directory: 'file.txt', хотя файл имеется
# удаляла задачу и заново создавала(файл на месте), ошибка. Пытаюсь решить.


