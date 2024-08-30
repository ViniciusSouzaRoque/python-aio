def plusOne(digit: list):
    return [int(digito) for digito in str(int(''.join(str(num) for num in digit)) + 1)]

digit = [1, 2, 3, 9]

print(plusOne(digit))