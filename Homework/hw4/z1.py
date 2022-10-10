""" Задача 1. Вычислить число c заданной точностью d    
Пример:    
при d = 0.001, π = 3.141    10^(-1) ≤ d ≤10^(-10)
"""

from cmath import pi 
import numpy
from decimal import Decimal 

print()
pi = numpy.pi
d = input("Введите число точности для округления числа pi:")
print()

def Accuracy(pi, d):
    accuracyPi = Decimal(pi)
    return accuracyPi.quantize(Decimal(d)) 
    
print("Число pi с точностью", d, " = ", Accuracy(pi, d))
print()



