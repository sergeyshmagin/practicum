# Задача Иосифа Флавия
# рекурсивное решение
# n - Колическво претендентов
# k - шаг
# def josephus(n, k):
#    return 0 if n == 0 else (josephus(n - 1, k) + k) % n


def counter(pretendents_count, iterations_count):

    result = 0
    for i in range(2, pretendents_count + 1):
        result = (result + iterations_count) % i
    return result + 1

with open('input.txt', 'r') as file_input:
    pretendents_count = int(file_input.readline())
    iterations_count = int(file_input.readline())
with open('output.txt', 'w') as file_output:
    file_output.write(str(counter(pretendents_count, iterations_count)))