# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#ДО:
# print()
# userN = int(input("Введите число N: "))

# def Factorial(userN): 
#     commonList = [] # в общий список будет сохранятся набор произведений
#     factorialUserN = 1 # первоначальное значение
#     for i in range(userN):
#         factorialUserN = factorialUserN*(i+1)
#         commonList.append(factorialUserN)
#     return(commonList)

# print("Произведение чисел от 1 до N равняется:", Factorial(userN))
# print()

#ПОСЛЕ:
print()
userN = int(input("Введите число N: "))
def Factorial(userN): 
    factorialUserN = (lambda i: 1 if i == 0 else i * factorialUserN(i - 1))
    commonList = list(factorialUserN(i) for i in range(1, userN + 1))
    return commonList
    
print("Произведение чисел от 1 до N равняется:", Factorial(userN))
print()


