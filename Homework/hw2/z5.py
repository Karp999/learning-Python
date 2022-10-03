# Задача 5. Реализуйте алгоритм перемешивания списка.

import random
print()

initialList = [1,2,3,4,5,6,7,8,9]
print(initialList)
for i in range(len(initialList)):
    k = initialList[i]
    position = random.randint(0,8)
    initialList[i] = initialList[position]
    initialList[position] = k
print(initialList)
