
def myAtoi(s: str) -> int:
    string_list = [digit for digit in s]

    while string_list and string_list[0] == " ":
        string_list.pop(0)

    is_positive = True
    
    if string_list:
        if string_list[0] == "-":
            is_positive = False
            string_list.pop(0)
        elif string_list[0] == "+":
            string_list.pop(0)


    while string_list and string_list[0] == '0':
        string_list.pop(0)

    if not string_list:
        return 0

    for index, value in enumerate(string_list):
        if value.isdigit():
            continue
        else:
            string_list = string_list[0:index]
            break

    max_negative = -2**31
    max_positive = 2**31 - 1

    result = int("".join(string_list)) if string_list else 0
    result = result if is_positive else result * -1

    if result > max_positive:
        return max_positive
    elif result < max_negative:
        return max_negative
    else:
        return result


s = "words and 987"
result = myAtoi(s)

print(result)