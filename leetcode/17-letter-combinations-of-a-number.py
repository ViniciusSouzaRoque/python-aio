from typing import List

digits_mapping = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def recursive_char_append(combination, next_digits):
            if not next_digits:
                output_list.append(combination)
                return
            for digit in digits_mapping[int(next_digits[0])]:
                recursive_char_append(combination + digit, next_digits[1:])

        output_list = []

        if digits:
            recursive_char_append("", digits)
        return output_list

digits = "23"
print(Solution().letterCombinations(digits))
