""" Задача 1. Решить уравнение:
f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
1. Определить корни
2. Найти интервалы, на которых функция возрастает
3. Найти интервалы, на которых функция убывает
4. Построить график
5. Вычислить вершину
6. Определить промежутки, на котором f > 0
7. Определить промежутки, на котором f < 0

"""
# 1. установить библиотеку sympy
# 2. from sympy import *
# 3. x = Symbol('x') - поможет сконструировать x
# 4. написать функцию, как бы мы написали в обычном питоне
# 5. построение графика - plot - как в лекции - from sympy.plotting import plot
# 6. кортеж




"""
С ЛЕКЦИИ
Руслан:
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import math

def task4_graph():
x = np.arange(-50, 50, 0.01)
plt.figure(figsize=(10, 5))
plt.plot(x, 5*x**2 + 10*x - 30, label=r'f(x) = 5x^2 + 10x - 30')

plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('figure_with_legend.png')
plt.show()

def task1_roots():
x = symbols('x')
ans = solve(5*x**2 + 10*x - 30, x)
print (ans)

///

x = symbols('x')
ans = solveset(-12*x**4*cos(x) - 18*x**3+5*x**2 + 10*x - 30, x)
print (ans)
Талипов Руслан: ConditionSet(x, Eq(-12*x**4*cos(x) - 18*x**3 + 5*x**2 + 10*x - 30, 0), Complexes)
Талипов Руслан: он выдает
"""
