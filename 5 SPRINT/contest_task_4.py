def max_blocks(arr):
    blocks = 0  # Количество блоков
    max_value = 0  # Текущий максимум в блоке

    # Проходим по всем элементам массива
    for i, value in enumerate(arr):
        # Обновляем максимум текущего блока
        max_value = max(max_value, value)
        # Если индекс i совпадает с текущим максимумом, блок завершён
        if max_value == i:
            blocks += 1

    return blocks


with open('input.txt', 'r') as file_input:
    dig_count = file_input.readline().split()
    arr = list(map(int, file_input.readline().split()))
with open('output.txt', 'w') as file_output:
    file_output.write(str(max_blocks(arr)))
