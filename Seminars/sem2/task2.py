# 2. Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.    
#     Пример:    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

some_dict = {}
n = int(input("n = "))
for i in range(1, n+1):
    some_dict[i] = 3 * i + 1
print(some_dict)

"""
print("Введите число N")
N = int(input())
#пустой словарь : d = {} 
d = dict()

for i in range(1,N+1):
    f = 3*i+1
    d[i] = f

print(d)
"""