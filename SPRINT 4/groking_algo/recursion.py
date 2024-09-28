def recrusion(data):
    # Пока массив не будет пуст

    # if not data:
    #     return 0
    # else:
    #     x = data.pop(0) + recrusion(data)

    # пока не останется 1 элемент в массиве
    if sum(data) == data[0]:
        return sum(data)
    else:
        x = data.pop(0) + recrusion(data)
    return x


data = [2, 3, 4, 5, 6, 5]
print(recrusion(data))
