""" Задача 1 . Прикрутить бота к задаче про конфеты.
    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
    Все конфеты оппонента достаются сделавшему последний ход. 

"""
# пыталась сделать жеребьевку - получилось, однако, не выходит перейти с жеребьевки к обращению к игроку
# постоянно ошибка вокруг строки:
# moveFirstPlayer = input(first, "Сколько вы возьмёте конфет? Введите число от 0 до 28: ")
# TypeError: input expected at most 1 argument, got 2
# нашла только что выход попробовать через конкатенацию

from random import randint
# Игра человек против человека.
print()
print("Приветствуем! Вы играете в игру '2021 конфета'.")
print("После жеребьёвки каждый из вас по очереди забирает не более 28 конфет.")
print("Побеждает тот, кто сделает крайний ход.")
print()
# # Жеребьёвка и ход игры.
# def GameProgress(firstPlayerCandy, secondPlayerCandy):
#     candy = 2021
#     if randint(0, 1) == 1:
#         first = "Ева"
#         second = "Адам"
#         print(first,", первый ход ваш.", second,", вы берёте конфеты после первого игрока .")
#     else:
#         first = "Адам"
#         second = "Ева"
#         print(first,", первый ход ваш.", second,", вы берёте конфеты после первого игрока .")

 candy = 2021
#     for i in range(candy+1):
#         #описание ходов первого игрока. 
#         moveFirstPlayer = int(input(first+", сколько вы возьмёте конфет? Введите число от 0 до 28: "))
#         if 0 <= moveFirstPlayer <= 28:
#             firstPlayerCandy = firstPlayerCandy + moveFirstPlayer
#             candy = candy - moveFirstPlayer
#             print (first+" имеет", firstPlayerCandy, "конфет. В игре осталось", candy,"конфет.")
#             print()
#         elif moveFirstPlayer > 28:
#             moveFirstPlayer = int(input(first+", взять можно от 0 до 28 конфет, повторите ход. Сколько вы возьмёте конфет? "))
#             firstPlayerCandy = firstPlayerCandy + moveFirstPlayer
#             candy = candy - moveFirstPlayer
#             print (first+" имеет", firstPlayerCandy, "конфет. В игре осталось", candy,"конфет.")
#             print()
#         elif moveFirstPlayer > candy:
#             moveFirstPlayer = int(input(first+", в стопке недостаточно конфет. Берите,"+candy+"конфет:"))
#             firstPlayerCandy = firstPlayerCandy + moveFirstPlayer
#             candy = candy - moveFirstPlayer
#             print (first+" имеет", firstPlayerCandy, "конфет. В игре осталось", candy,"конфет.")
#             print()
#         elif candy == 0:
#             firstPlayerCandy = firstPlayerCandy + secondPlayerCandy
#             print(first+", поздравляем, вы победили и все конфеты ваши!:) Игра окончена!")
#             print()
#             return
        

#         # Описание ходов второго игрока.
#         moveSecondPlayer = int(input(second+", сколько вы возьмёте конфет? Введите число от 0 до 28: "))
#         if 0 <= moveSecondPlayer <= 28:
#             secondPlayerCandy = secondPlayerCandy + moveSecondPlayer
#             candy = candy - moveSecondPlayer
#             print (second+" имеет", secondPlayerCandy, "конфет. В игре осталось", candy,"конфет.")
#             print()
#         elif moveSecondPlayer > 28:
#             moveSecondPlayer = int(input(second+", взять можно от 0 до 28 конфет, повторите ход. Сколько вы возьмёте конфет? "))
#             secondPlayerCandy = secondPlayerCandy + moveSecondPlayer
#             candy = candy - moveSecondPlayer
#             print (second+" имеет", secondPlayerCandy, "конфет. В игре осталось", candy,"конфет.")
#             print()
#         elif moveSecondPlayer > candy:
#             moveSecondPlayer = int(input(first+", в стопке недостаточно конфет. Берите,"+candy+"конфет:"))
#             secondPlayerCandy = secondPlayerCandy + moveSecondPlayer
#             candy = candy - moveSecondPlayer
#             print (second+" имеет", secondPlayerCandy, "конфет. В игре осталось", candy,"конфет.")
#             print()
#         elif candy == 0:
#             secondPlayerCandy = firstPlayerCandy + secondPlayerCandy
#             print(second+", поздравляем, вы победили и все конфеты ваши!:) Игра окончена!")
#             print()
#             return
#     return
        
             

# firstPlayerCandy = 0 
# secondPlayerCandy = 0
# print("Игра началась, удачи!:)", GameProgress(firstPlayerCandy, secondPlayerCandy))
# print()
# -----
def pve_mode(comp_candy, player_candy):
    candy = 2021
    print("Игра с Ботом!")
    while candy > 0: 
        take1_candy = randint(0, 28)
        if take1_candy>candy:
            take1_candy=candy
        print("Бот берет"+candy+"конфет.")
        comp_candy = comp_candy + take1_candy
        candy = candy - take1_candy
        print (" Бот имеет", comp_candy, "конфет. В игре осталось", candy,"конфет.")
        print()
        if candy == 0:
            player = comp_candy+player
            print("Бот победил! Игра окончена!")
            return
        take2_candy = int(input(", сколько вы возьмёте конфет? Введите число от 0 до 28: "))
        while take2_candy <=0 or take2_candy >28:
            take2_candy = int(input(", взять можно от 0 до 28 конфет, повторите ход. Сколько вы возьмёте конфет? "))
        while take2_candy > candy:
            take2_candy = int(input("в стопке недостаточно конфет, повторите ход. Сколько вы возьмёте конфет? "))
        else:
            if 0 <= take2_candy <= 28:
                player = take2_candy+player
                candy = candy-take2_candy
                print (" Бот имеет", player, "конфет. В игре осталось", candy,"конфет.")
                if candy == 0:
                    player = player+comp_candy
                    print(", поздравляем, вы победили и все конфеты ваши!:) Игра окончена!")
                    return
    return

