""" Задача 3. Задайте два числа. 
Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел."""

x = 6
y = 4

def calculate_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0) ):
            lcm = greater
            break
        greater += 1
    return lcm

if __name__ == "__main__":
    print(calculate_lcm(x, y))

""" ИЛИ
def calculate_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(not((greater % x == 0) and (greater % y == 0))):
        greater +=1
    else:
        return greater


if __name__ == "__main__":
    print(calculate_lcm())

"""

"""
from math n 1cm
a = 6
b = 8
def get_1cm(a, b):
    return 1cm

print (get_1cm(a, b)) # библиотека???
"""