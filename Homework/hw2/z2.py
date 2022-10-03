# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from re import I


print()
userN = int(input("Введите число N: "))

def Factorial(userN): # решила сделать через факториал
    factorialUserN = 1 # первоначальное значение
    for i in userN:
        factorialUserN *= int(i) 
        return(i)

print("Произведение чисел от 1 до N равняется:", Factorial(userN))

