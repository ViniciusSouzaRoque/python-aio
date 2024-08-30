

class Solution:
    def isValid(self, s: str) -> bool:
        looking_for = []

        mapped_values = {
            '{': '}',
            '(': ')',
            '[': ']'
        }

        for value in s:
            if value in mapped_values.keys():
                looking_for.append(mapped_values[value])

            if value in mapped_values.values():
                if looking_for and looking_for.pop() == value:
                    continue
                else:
                    return False

        return True if not looking_for else False


my_input = "()"

my_solution = Solution()
print(my_solution.isValid(my_input))