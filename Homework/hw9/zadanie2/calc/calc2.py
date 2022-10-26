def create_list():
    print('С клавиатуры введите список элементов, по окончанию ввода нажмите Enter')
    list = []
    for i in range(3):
        list.append(str(input('> ')))
    record_log(str(list[0]+list[1]+list[2]))
    return list

def check_list():
    if text2[i].find('абв') == -1:

def record_log(log):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(log + '\n')

def main():
    list = create_list()
    check_list(list)
    print(list)
    # print(f'Сумма элементов расположенных на нечетных позициях = {sum_odd(list)}')

main()