# Задача 3. Задайте список из n чисел последовательности (1+ 1/n)^n 
# и выведите на экран их сумму (округляйте до 3 знаков после запятой).    
# Пример:    
# Для n = 6: [2, 2.25, 2.37, 2.441, 2.488, 2.522]

print()
userN = int(input("Введите количество позиций для создания списка последовательности (1+1/n)^n: "))
print()

commonList = []
def Sequence(userN):
    for i in range(1,userN+1):
        commonList.append(round((1+1/i)**i,3))
    return(commonList)
print ("Вывод последовательности: ", Sequence(userN))
print()

sum = 0
for i in range(userN):
    sum = sum + commonList[i]
print("Сумма чисел последовательности (1+1/n)^n равна:", sum)
print()





