""" Задача 3. Напишите программу, которая определит позицию 
второго вхождения строки в списке либо сообщит, что её нет.
Пример:
- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1
"""

print()
commonList = ["qwe", "ujn", "zxc", "qwe", "ertqwe"] #перебирает индекс или результат??
def Func (string):
    count = 0
    for i in range(len(commonList)):
        if commonList[i] == string:
            count +=1

        if count == 2:
            return i
    return -1

print(Func(input("Введите символ:")))
print()