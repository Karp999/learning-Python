# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.    
# Пример:    
# 6782 -> 23
# 0,56 -> 11

print()
userNum = input("Введите число: ")
# хотела сделать ввод через float, но в функции выдаёт ошибку 'float' object has no attribute 'replace'

def DigitSum(userNum):
    sum = 0
    userNum = userNum.replace(",", ".")
    index = len(userNum) 
    print(index) # для меня, проверяю количество введённых позиций 
    for index in userNum:
        if index != ".":
            sum += int(index)
    return(sum)

print("Сумма цифр введённого числа равняется: ", DigitSum(userNum))
print()



