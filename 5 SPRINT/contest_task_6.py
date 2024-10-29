def orders_processing(orders_arr, samples_arr: list):
    counter = 0
    orders_arr = sorted(orders_arr)
    samples_arr = sorted(samples_arr)
    i, j = 0, 0

    while i < len(orders_arr) and j < len(samples_arr):
        if orders_arr[i] <= samples_arr[j]:
            counter += 1
            i += 1
        j += 1
    return counter


with open('input.txt', 'r') as file_input:
    orders_count = int(file_input.readline())
    orders_arr = [int(i) for i in file_input.readline().split()]
    sample_count = int(file_input.readline())
    samples_arr = [int(i) for i in file_input.readline().split()]
with open('output.txt', 'w') as file_output:
    file_output.write(str(orders_processing(orders_arr, samples_arr)))
