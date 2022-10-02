# Задача 5. Напишите программу, которая принимает на вход число и проверяет, 
# кратно ли оно 5 и 10 или 15, но не 30.

number = int(input("число - "))
if (number % 5 == 0 and number % 10 == 0 and number % 30 != 0) or (number % 15 == 0 and number % 30 != 0):
    print(True)
else:
    print(False)


#number = int(input("число - "))
#def someFunc(n):
#   if (number % 5 == 0 and number % 10 == 0 and number % 30 != 0) or (number % 15 == 0 and number % 30 != 0):
#      return True
#    else:
#        return False

#print(someFunc(number))