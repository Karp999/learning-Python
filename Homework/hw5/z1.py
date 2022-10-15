""" Задача 1 . Создайте программу для игры с конфетами человек против человека.    
    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
    Все конфеты оппонента достаются сделавшему последний ход. 
    Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?    
    a) Добавьте игру против бота    
    b) Подумайте как наделить бота "интеллектом"    
"""
from random import randint
# Игра человек против человека.
print()
print("Приветствуем! Вы играете в игру '2021 конфета'.")
print("После жеребьёвки каждый из вас по очереди забирает не более 28 конфет.")
print("Побеждает тот, кто сделает крайний ход.")
print()
# Жеребьёвка и ход игры.
def GameProgress(firstPlayerCandy, secondPlayerCandy):
    candy = 2021
    if randint(0, 1) == 1:
        first = "Ева"
        second = "Адам"
        print(first, ", первый ход ваш.", second, ", вы берёте конфеты после первого игрока .")
    else:
        first = "Адам"
        second = "Ева"
        print(first, ", первый ход ваш.", second, ", вы берёте конфеты после первого игрока .")


    for i in range(candy+1):
        # Описание ходов Евы.
        # while take1_candy > candy:
        #     print("в стопке недостаточно конфет")
        #     take1_candy = int(input("Первый игрок берет ? конфет: "))
        moveFirstPlayer = int(input("Ева, сколько вы возьмёте конфет? Введите число от 0 до 28: "))
        if 0 <= moveFirstPlayer <= 28:
            firstPlayerCandy = firstPlayerCandy + moveFirstPlayer
            i = candy - moveFirstPlayer
            print ("У Евы", firstPlayerCandy, "конфет. В игре осталось", i,"конфет.")
        if moveFirstPlayer > 28:
            print("Ева, взять можно от 0 до 28 конфет, повторите ход.")
        if candy == 0:
            firstPlayerCandy = firstPlayerCandy + secondPlayerCandy
            print("Ева, поздравляем, вы победили и все конфеты ваши!:) Игра окончена!")
            return
        

        # Описание ходов Адама.
        moveSecondPlayer = int(input("Адам, сколько вы возьмёте конфет? Введите число от 0 до 28: "))
        if 0 <= moveSecondPlayer <= 28:
            secondPlayerCandy = secondPlayerCandy + moveSecondPlayer
            i = candy - moveSecondPlayer
            print ("У Адама", secondPlayerCandy, "конфет. В игре осталось", i,"конфет.")
        if moveSecondPlayer > 28:
            print("Адам, взять можно от 0 до 28 конфет, повторите ход.")
        if candy == 0:
            secondPlayerCandy = firstPlayerCandy + secondPlayerCandy
            print("Адам, поздравляем, вы победили и все конфеты ваши!:) Игра окончена!")
            return
    return
        
             

firstPlayerCandy = 0 
secondPlayerCandy = 0
print("Игра началась, удачи!:)", GameProgress(firstPlayerCandy, secondPlayerCandy))
print()