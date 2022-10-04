# 3. Напишите программу, в которой пользователь будет задавать две строки,
#  а программа - определять количество вхождений одной строки в другой.

str_one = 'good news everyone, or one'
str_two = 'one'
#S.find(str, [start],[end])  - поиск
count = 0
index = 0 # индексы вхождения 15 и 26 должны быть
start = index
while index != -1: #"если не нашлось вхождение,функция find выдаст -1",-Михаил
    if str_one.find(str_two, start+1)!=-1 : #start+1 -с 16  дальнейший поиск, чтобы второй раз на 15 не попасть
        index = str_one.find(str_two, start+1) #тут мы и присваиваем новый индекс-16
        start = index
        count +=1 #счетчик увеличиваем на 1,тк нашли ещ1 вхождение
    else:
        index = -1
print(count)

"""

"""