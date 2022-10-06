""" Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.    
Пример:    
45 -> 101101
3 -> 11
2 -> 10
"""
print()
userN = int(input("Введите число: "))
print()

def DecimalToBinary (num):
    binaryList = []
    while num > 0:
        remainder = num % 2
        binaryList.append(remainder)

    for i in range(len(binaryList)//2): 
        temp = binaryList [i]
        binaryList[i] = binaryList[len(binaryList) - i - 1]
        binaryList[len(binaryList) - i - 1] = temp

    return binaryList

print("Десятичное число", userN,"в двоичной системе счисления равно:", DecimalToBinary(userN))
print()
