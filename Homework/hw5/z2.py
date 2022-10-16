""" Задача 2 . Создайте программу для игры в "Крестики-нолики"."""

from random import randint

# ПРИВЕТСТВИЕ
print()
print("Приветствуем! Вы играете в игру «Крестики-нолики».")
print("Игроки по очереди заполняют клетки поля. Один игрок - «крестиками», второй - «ноликами».")
print("Побеждает тот, кто первый заполнит три клетки своим знаком по вертикали, горизонтали или диагонали.")
print("Игра началась, удачи!:)")
print()

# ОПИСАНИЕ ПОЛЯ
# для удобства пользования полем прономеруем каждую клетку. Клеток 9, создадим лист из 9 элементов по возрастанию.
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# отображение поля
def Mapping():
    print("-" * 13)
    print("|", field[0], "|", field[1], "|", field[2], "|")
    print("-" * 13)
    print("|", field[3], "|",  field[4], "|",  field[5], "|")
    print("-" * 13)
    print("|", field[6], "|",  field[7], "|",  field[8] , "|" )
    print("-" * 13)
# индексы вертикалей, горизонталей, диагоналей, которые приведут к победе в игре.
winningPosition = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7], [2, 4, 6], [2, 5, 8], [3, 4, 5], [6, 7, 8]]


# ХОД ИГРЫ
def GameProgress(first):
    if randint(0, 1) == 1:
        first = "Ева"
        second = "Адам"
        print(first, ", первый ход ваш.", second, ", вы берёте конфеты после первого игрока .")
    else:
        first = "Адам"
        second = "Ева"
        print(first, ", первый ход ваш.", second, ", вы берёте конфеты после первого игрока .")

    value = False
    while not value:
        moveFirstPlayer = input(first, ", какую клетку вы выберете? Введите число от 1 до 9: ")
        try:
            moveFirstPlayer = int(moveFirstPlayer)
        except:
            print("Вы ввели некорректное значение. Попробуйте еще раз.")
            continue
        if 9 >= moveFirstPlayer >= 1:
            if(str(field[moveFirstPlayer - 1]) not in ("XO")):
                field[moveFirstPlayer - 1] = first
                value = True
            else:
                print("Невозможно выполнить ход в уже заполненную ячейку. Попробуйте еще раз.")
        else:
            print("Такой ячейки не существует. Попробуйте еще раз.")

#ПРОВЕРКА ПОБЕДЫ 
def VictoryCheck(field, winningPosition):
    for all in winningPosition:
        if field[all[0]] == field[all[1]] == field[all[2]]:
            return field[all[0]]
    return False

