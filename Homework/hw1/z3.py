# Задача 3: Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).    
#    Пример:    
#    x=34; y=-30 -> 4
#    x=2; y=4-> 1
#    x=-34; y=-30 -> 3

userX = int(input("Введите x:"))
print(userX)
userY = int(input("Введите y:"))
print(userY)

def GetQuoterFromCoordinate(userX, userY):
    if userX>0 and userY>0:
        return("Точка пересечения координат находится в четверти № 1.")
    elif userX<0 and userY>0:
        return("Точка пересечения координат находится в четверти № 2.")
    elif userX<0 and userY<0:
        return("Точка пересечения координат находится в четверти № 3.")
    elif userX>0 and userY<0:
        return("Точка пересечения координат находится в четверти № 4.")
    else: 
        return("Невозможно определить четверть: точки координат не должны равняться 0. ")

print(GetQuoterFromCoordinate(userX, userY))



