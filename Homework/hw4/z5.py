""" Задача 5. Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов."""

# Не разобралась в четвертой задаче, поэтому не могу воспользоваться 
# сформированными файлами с многочленами (а хотелось). 
# Создала дополнительно два файла с предварительно записанными многочленами для попытки решения пятой задачи,
# написала функцию их чтения, а дальше опять ступор.

firstP = "firstPforz5.txt"
secondP = "secondPforz5.txt"

def ReadingFiles(file):
    data = open(file, "r")
    for line in data:
        print(line)
    data.close()


print(ReadingFiles(firstP))
print(ReadingFiles(secondP))

"""
def read_file():
    eq1 = open_file("text.txt") # прочитаем нашу строчку с формулой из файла
    print("первый многочлен", eq1)
    eq1 = eq1[:-2].split("+") #отделим = 0 и разобьем по знаку +
    eq2 = open.file("text1.txt")
    print("второй многочлен", eq2)
    eq2 = eq2[:-2].split("+") #отделим = 0 и разобьем по знаку +

dict1 = separate_equa(eq1)
dict2 = separate_equa(eq2)
# эта проверка необходима,чтобы посмотреть,где больше ключей(членов с x)
if len(dict1.keys()) > len(dict2.keys())
    (normalize(addition_eq(dict1, dict2)))
else:
    (normalize(addition_eq(dict2, dict1)))


def open_file(name)
    f = open(name, "r")
    equa = f.read()
    f.close
    return equa

def separate_equa(equa): #оставим только ключ(степень x) значение(коэф,он же множитель)
    dict_eq = {}
    for el in equa:
        

"""