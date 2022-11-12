from random import randint

def Lottery():
    a = randint(0, 1)
    if a == 1:
        print("Первый ход ваш!")
    else:
        print("Первым ходит Бот, ваш ход следующий.")

