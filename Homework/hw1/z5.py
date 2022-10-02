# Задача 5: Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.    
# Пример:    
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

userX1 = int(input("Введите x1: "))
print(userX1)
userX2 = int(input("Введите x2: "))
print(userX2)
userY1 = int(input("Введите y1: "))
print(userY1)
userY2 = int(input("Введите y2: "))
print(userY2)

def Distance(userX1, userX2, userY1, userY2):
    dist = ((userX2-userX1)**2+(userY2-userY1)**2)**0.5
    return(round(dist, 2))

print(Distance(userX1, userX2, userY1, userY2))

