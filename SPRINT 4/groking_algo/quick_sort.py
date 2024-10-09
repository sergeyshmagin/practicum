from random import randint as rnd 
def quicksort(arr):
    # Базовый случай: массив меньше 2-х элементов
    if len(arr) < 2:
        return arr
    else:
        # Опорная точка
        # pivot = arr[0] первый элемент массива
        pivot = arr[rnd(0, len(arr))] # случайный элемент массива. Работает быстрее O(n * log n)
        less = [i for i in arr if i < pivot]
        more = [i for i in arr if i > pivot]
        return quicksort(less) + [pivot] + quicksort(more)


arr = [50, 4, 2, 34, 65, 21, 35, 19, 100, 1]
print(quicksort(arr))
