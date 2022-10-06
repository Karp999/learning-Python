""" Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.    
Пример:    
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
[Негафибоначчи](https://ru.wikipedia.org/wiki/Негафибоначчи)
"""
print()
userN = int(input("Введите число: "))
print()

def Fib(userN): 
    if userN in [1, 2]:
        return 1
    else:
        return Fib(userN-1) + Fib(userN -2)

list = [] #для будущего списка чисел Фибоначчи и Негафибоначчи
for k in range(1, userN + 1):
    list.append(Fib(k))

def NegaFib(list):
    listN = [] #для работы именно с Негафибоначчи
    for i in range(len(list)): 
        if (len(list) - i - 1) % 2 != 0:
            listN.append(-list[-i-1])
        else:
            listN.append(list[-i-1])
    listN.append(0) 
    for i in range(len(list)): 
        listN.append(list[i])
    return listN

print("Список чисел Фибоначчи с положительными и отрицательными индексами:")
print(NegaFib(list))
print()



