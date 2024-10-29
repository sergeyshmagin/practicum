def insertion_sort(sort_arr_count, sort_arr, example_arr_len, example_arr):

    result_arr = []
    temp_arr = []

    for j in example_arr:
        temp_arr = [i for i in sort_arr if i == j]
        result_arr = result_arr + temp_arr

    temp_arr = [i for i in sort_arr if i not in result_arr]

    for i in range(1, len(temp_arr)):
        current = temp_arr[i]
        prev = i - 1
        while prev >= 0 and temp_arr[prev] > current:
            temp_arr[prev + 1] = temp_arr[prev]
            prev -= 1
        temp_arr[prev + 1] = current

    result_arr = result_arr + temp_arr
    return ' '.join(str(e) for e in result_arr)


with open('input.txt', 'r') as file_input:
    sort_arr_count = int(file_input.readline())
    sort_arr = list(map(int, file_input.readline().split()))
    example_arr_len = int(file_input.readline())
    example_arr = list(map(int, file_input.readline().split()))

with open('output.txt', 'w') as file_output:
    result = insertion_sort(sort_arr_count, sort_arr, example_arr_len, example_arr)
    file_output.write(result)
# print(insertion_sort(sort_arr_count, sort_arr, example_arr_len, example_arr))
