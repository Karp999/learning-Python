""" Задача 1. Решить уравнение:
f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
1. Определить корни.
2. Найти интервалы, на которых функция возрастает.
3. Найти интервалы, на которых функция убывает.
4. Построить график.
5. Вычислить вершину.
6. Определить промежутки, на котором f > 0.
7. Определить промежутки, на котором f < 0.
"""
from sympy import *

x = Symbol("x")
f = -12 * x**4 *sin(cos(x)) - 18 * x**3 + 5 * x**2 + 10 * x - 30
plot(f, (x, -5, 5))
solution = solve(f, x)
print(solution)
interv = Interval(int(solution[1]-1),int(solution[0]+1))
res_min = minimum(f,x,interv)
print(res_min)
