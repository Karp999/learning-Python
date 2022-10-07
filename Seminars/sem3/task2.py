"""Задача 2. Задайте список. Напишите программу, которая определит, 
присутствует ли в заданном списке строк некое число."""

print()
commonList = ["tor",51, "51", "toryanski", "1Tor6"]
def Func (commonList):
    for item in commonList:
        if isinstance(item, int) or isinstance(item, float):
            return "Yes"
        
    return "No"

print(Func(commonList))
print()