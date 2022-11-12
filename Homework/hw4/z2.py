""" Задача 2. Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N."""

print()
userN = int(input("Введите натуральное число N: "))
print()

def Factorization (userN):
    listOfPrimeFactors = []
    m = 2 
    while userN > 1:
        if userN % m == 0:
            userN = userN // m 
            listOfPrimeFactors.append(m) 
        else:
            m += 1
    return listOfPrimeFactors

print ("Список простых множителей числа N:", Factorization (userN))
print()



