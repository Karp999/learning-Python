""" Задача 3 . Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности."""

print()
initialList = [1, 2, 9, 7, 4, 2, 3, 4, 2, 8, 8, 2, 1]
print(initialList)
print()

def NonRecurring(initialList):
    result = []
    listToDict = {}.fromkeys(initialList, 0)

    for i in initialList:
        listToDict[i] += 1

    for g in listToDict:
        if listToDict[g] == 1:
            result.append(g)
    return result

print("Список неповторяющихся элементов исходной последовательности:", NonRecurring(initialList))
print()



# print("Список неповторяющихся элементов исходной последовательности:", NonRecurring(initialList))
# print()

# Хотела попробовать преобразовать через множества, но удаляет только дубликаты, оставляя один вариант:
#
# print()
# initialList = [1, 2, 9, 7, 4, 2, 3, 4, 2, 8, 8, 2, 1]
# print("Первоначальный список: ", initialList)
# newSet = set(initialList)
# print("Преобразование во множество: ", newSet)
# newList = list(newSet)
# print("Преобразование в новый список без дубликатов: ", newList)
#
# Терминал:
# Первоначальный список:  [1, 2, 9, 7, 4, 2, 3, 4, 2, 8, 8, 2, 1]
# Преобразование во множество:  {1, 2, 3, 4, 7, 8, 9}
# Преобразование во множество:  [1, 2, 3, 4, 7, 8, 9]
#
# Потом хотела сравнить списки ,получившиеся при преобразовании список vs список-множество-список 
# и удалить повторяющиеся элементы. Застопорилась:
#  
# def NonRecurring(initialList):
#     newNewList = []
#     for i in initialList:
#         for k in newList:
#             if initialList[i] != newList[k]:
#                 # newList.remove(k)
#                 newNewList.append(i)
#     print(newNewList)

# print("Список неповторяющихся элементов исходной последовательности:", NonRecurring(initialList))
# print()


