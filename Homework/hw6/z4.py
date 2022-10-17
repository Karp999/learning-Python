# Задача с семинара 2: 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность
#  из N членов, подчиняющихся закону f(i) = 3^i*(-1)^i,  где i - индекс элемента последовательности.    
#     Пример:    
#     - Для N = 5: 1, -3, 9, -27, 81

# #ДО:
# n = int(input("enter n ="))
# some_list = []
# for i in range (0, n):
#     some_list.append((-3)**i)
# print(some_list)

#ПОСЛЕ:
n = int(input("enter n ="))
some_list = list(map(lambda i: (-3)**i, range (0, n))) #взяла эту задачу для тренировки map() и lambda
print(some_list)