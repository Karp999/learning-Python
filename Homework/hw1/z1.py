# Задача 1: Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

userNumber = int(input('Введите число от 1 до 7: '))
print(userNumber)
if userNumber == 1:
    print ("Понедельник - рабочий день.")
elif userNumber == 2:
    print ("Вторник - рабочий день.")
elif userNumber == 3:
    print ("Среда - рабочий день.")
elif userNumber == 4:
    print ("Четверг - рабочий день.")
elif userNumber == 5:
    print ("Пятница - рабочий день.")
elif userNumber == 6:
    print ("Суббота - выходной.")
elif userNumber == 7:
    print ("Воскресенье - выходной.")
else:
    print("Нет такого дня недели!")