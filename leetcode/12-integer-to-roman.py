
numbers_roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

diff_roman = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}

def convert_to_roman(num: int):
    result = ''

    while num > 0:
        if str(num)[0] not in ('9', '4'):
            for key, value in reversed(numbers_roman.items()):
                while num >= value and str(num)[0] not in ('9', '4'):
                    result += key
                    num -= value
        else:
            for key, value in reversed(diff_roman.items()):
                if num >= value and str(num)[0] in ('9', '4'):
                    result += key
                    num -= value

    return result

print(convert_to_roman(45))