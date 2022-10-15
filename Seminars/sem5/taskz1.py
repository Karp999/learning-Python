""" Задача 1 . Создайте программу для игры с конфетами человек против человека.    
    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
    Все конфеты оппонента достаются сделавшему последний ход. 
    Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?    
    a) Добавьте игру против бота    
    b) Подумайте как наделить бота "интеллектом"    
"""

from random import randint

def pvp_mode (player_candy, player2_candy):
    print("PVP mode!")
    candy = 2021
    while candy > 0:
        take1_candy = int(input("Первый игрок берет ? конфет: "))
        while take1_candy <=0 or take1_candy > 28:
            print("Брать можно только от 0 до 28 конфет")
            take1_candy = int(input("Первый игрок берет ? конфет: "))
        while take1_candy > candy:
            print("в стопке недостаточно конфет")
            take1_candy = int(input("Первый игрок берет ? конфет: "))
        else:
            if 0 <= take1_candy <= 28:
                player_candy = player_candy + take1_candy
                candy = candy - take1_candy
                print ("У первого игрока", player_candy, "конфет")
                print("в стопке осталось конфет", candy)
                if candy == 0:
                    player_candy = player_candy + player2_candy
                    print("первый игрок победил, количество конфет:", player_candy, "игра окончена!")
                    return
        take2_candy = int(input("Второй игрок берет ? конфет: "))
        while take2_candy <=0 or take2_candy > 28:
            print("Брать можно только от 0 до 28 конфет")
            take2_candy = int(input("второй игрок берет ? конфет: "))
        while take2_candy > candy:
            print("в стопке недостаточно конфет")
            take2_candy = int(input("второй игрок берет ? конфет: "))
        else:
            if 0 <= take2_candy <= 28:
                player2_candy = player2_candy + take2_candy
                candy = candy - take2_candy
                print ("У второго игрока", player2_candy, "конфет")
                print("в стопке осталось конфет", candy)
                if candy == 0:
                    player2_candy = player2_candy + player_candy
                    print("второй игрок победил, количество конфет:", player2_candy, "игра окончена!")
                    return


def pve_mode (comp_candy, player_candy):
    print("PVE mode!")
    candy = 2021
    while candy > 0:
        take1_candy = randint(0,28)
        if take1_candy > candy:
            take1_candy = candy
        print("Компьютер берет ? конфет: ", take1_candy)
        comp_candy = comp_candy + take1_candy
        candy = candy - take1_candy
        print ("У компьютера", comp_candy, "конфет")
        print("в стопке осталось конфет", candy)
        if candy == 0:
            player1_candy = player_candy + comp_candy
            print("компьютер победил, количество конфет:", player1_candy, "игра окончена!")
            return
        take2_candy = int(input(" игрок берет ? конфет: "))
        while take2_candy <=0 or take2_candy > 28:
            print("Брать можно только от 0 до 28 конфет")
            take2_candy = int(input("игрок берет ? конфет: "))
        while take2_candy > candy:
            print("в стопке недостаточно конфет")
            take2_candy = int(input("второй игрок берет ? конфет: "))
        else:
            if 0 <= take2_candy <= 28:
                player_candy = player_candy + take2_candy
                candy = candy - take2_candy
                print ("У второго игрока", player_candy, "конфет")
                print("в стопке осталось конфет", candy)
                if candy == 0:
                    player_candy = player_candy + comp_candy
                    print("игрок победил, количество конфет:", player_candy, "игра окончена!")
                    return

def mode_sel(mode):
    if mode == 1:
        player_candy = 0
        player2_candy = 0
        pvp_mode (player_candy, player2_candy)
    elif mode == 2:
        comp_candy = 0
        player_candy = 0
        pve_mode (comp_candy, player_candy)
    else:
        print("нет такого режима!")

modesel = int(input("выбери режим игры:\n1-против другого игрока\n2-против компьютера\nВыбор: "))
mode_sel(modesel)