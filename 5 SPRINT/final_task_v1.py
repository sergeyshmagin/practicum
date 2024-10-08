# ID посылки с успешным выполнением 120026613

DIGITS = '0123456789'


def decode_instructions(s: str) -> str:
    '''Function decodes instructions in a tasks queue'''
    stack: list[tuple[str, int]] = []
    current_num: int = 0
    current_str: str = ""

    for char in s:
        if char in DIGITS:
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            prev_str, repeat_times = stack.pop()
            current_str = prev_str + current_str * repeat_times
        else:
            current_str += char

    return current_str


with open('input.txt', 'r') as file_input:
    input_arr = [i for i in file_input.readline()]
with open('output.txt', 'w') as file_output:
    file_output.write(decode_instructions(input_arr))
