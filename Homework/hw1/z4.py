# Задача 4: Напишите программу, которая по заданному номеру четверти показывает 
# диапазон возможных координат точек в этой четверти (x и y).

userQuoter = int(input("Введите номер четверти прямоугольной системы координат от 1 до 4: "))
print(userQuoter)

def GetCoordinateFromQuoter(userQuoter):
    if userQuoter == 1:
        return("Диапазон координат: x>0 и y>0 .")
    elif userQuoter == 2:
        return("Диапазон координат: x<0 и y>0 .")
    elif userQuoter == 3:
        return("Диапазон координат: x<0 и y<0 .")
    elif userQuoter == 4:
        return("Диапазон координат: x>0 и y<0 .")
    else:
        return("В системе координат количество четвертей четыре, повторите попытку.")

print(GetCoordinateFromQuoter(userQuoter))