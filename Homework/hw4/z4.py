""" Задача 4 . Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.    
Пример:    
k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0
"""

# Не разобралась в задаче. Загуглила, попробовала разобрать и похожим вариантом решить.
# Всё равно не совсем поняла работу найденных решений (в интернете везде схожее решение).
# По данному решению у меня файлы не заполняются.
# (взяла в пример создание двух файлов, чтобы в пятой задаче ими воспользоваться)
# Выдает ошибку < can't multiply sequence by non-int of type 'list' >

from random import randint
import itertools

print()
k = 2

def getRatios(k):
    ratios = [randint(0, 100) for i in range(k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 100)
    return ratios

def Polynomial(k, ratios):
    formPolynomial =  ["*x"]*["x"]+["x"]*(["x"]**k) #пробовала = x**k+x
    p = [[a, b, c] for a, b, c in itertools.zip_longest(ratios, formPolynomial, range(k, 1, -1), fillvalue = " ") if a != 0]
    for x in p:
        x.append(" + ")
    p = list(itertools.chain(*p))
    p[-1] = " = 0"
    return "".join(map(str, p)).replace(" 1*x ", " x ")


polynomFirst = Polynomial(k, getRatios(k))
print("Многочлен степени", k, "=", polynomFirst)


polynomSecond = Polynomial(k, getRatios(k))
print("Многочлен степени", k, "=", polynomSecond)

# сохраняем ответы в файлы для следующей задачи
with open("polynomFirst.txt", "w") as data:
    data.write(polynomFirst)

with open("polynomSecond.txt", "w") as data:
    data.write(polynomSecond)


