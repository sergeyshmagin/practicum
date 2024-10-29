# ID посылки с успешным выполнением 120072652
import string


def decode_instructions(input_arr: list[str]) -> str:
    '''Function decodes instructions in a tasks queue'''
    stack: list[tuple[str, str]] = []
    current_str = current_num = ''

    for char in input_arr:
        if char in string.digits:
            current_num += char
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = current_num = ''
        elif char == ']':
            prev_str, repeat_times = stack.pop()
            current_str = prev_str + current_str * int(repeat_times)
        else:
            current_str += char

    return current_str


if __name__ == '__main__':
    with open('input.txt', 'r') as file_input:
        input_arr = [i for i in file_input.readline()]
    with open('output.txt', 'w') as file_output:
        file_output.write(decode_instructions(input_arr))
