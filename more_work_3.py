def func_max(*args):
    list_1 = input('Введите все нужные числа: ')
    list_1 = list_1.split()
    list_1 = list(map(int, list_1))
    max_number = list_1[0]
    for i in list_1:
        if max_number < i:
            max_number = i
        else:
            continue
    print(sorted(list_1, reverse=True))
    print(max_number)

func_max()