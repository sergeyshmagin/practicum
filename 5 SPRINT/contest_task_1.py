# Вычисление числа фибоначи. Рекурсия

def fibonacci(n):
    if n in (0, 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


with open('input.txt', 'r') as file_input:
    version = int(file_input.readline())

with open('output.txt', 'w') as file_output:
    file_output.write(str(fibonacci(version)))
