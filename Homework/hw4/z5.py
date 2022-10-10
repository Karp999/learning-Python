""" Задача 5. Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов."""

# Не разобралась в четвертой задаче, поэтому не могу воспользоваться 
# сформированными файлами с многочленами (а хотелось). 
# Создала дополнительно два файла с предварительно записанными многочленами для попытки решения пятой задачи.

firstP = "firstPforz5.txt"
secondP = "secondPforz5.txt"

def ReadingFiles(firstP, secondP):
    with open(str(firstP), 'r') as data:
        pfirst = data.read()
    with open(str(secondP), 'r') as data:
        psecond = data.read()
    return pfirst , psecond

print(ReadingFiles(firstP, secondP))
