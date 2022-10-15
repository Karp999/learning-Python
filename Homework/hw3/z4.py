""" Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.    
Пример:    
45 -> 101101
3 -> 11
2 -> 10
"""
print()
userN = int(input("Введите число: "))
print()

def DecimalToBinary(userN):
    binaryList = []
    while userN > 0: 
        remainder = userN % 2
        userN = userN // 2
        binaryList.append(remainder)

    for i in range(len(binaryList)//2): 
        k = binaryList [i] # k - временная переменная для пузырькового метода
        binaryList[i] = binaryList[len(binaryList) - i - 1]
        binaryList[len(binaryList) - i - 1] = k
        return binaryList

print("Десятичное число", userN,"в двоичной системе счисления равно:", DecimalToBinary(userN))
print()


