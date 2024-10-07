# Бинарный поиск с рекурсией


wins = ['Алгоритмист', 'Антон', 'жил', 'на', 'полигоне', 'пятьсот', 'суток']
my_ticket = 'Антон'


def binary_search(arr, x, left, right):
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    if x < arr[mid]:
        binary_search(arr, x, left, mid - 1)
    else:
        return binary_search(arr, x, mid + 1, right)


index = binary_search(wins, my_ticket, left=0, right=(len(wins) - 1))
print(index)
