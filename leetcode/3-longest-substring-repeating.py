
def get_next_repeat(str_list):
    new_list = []
    for value in str_list:
        if not value in new_list:
            new_list.append(value)
            continue
        break

    return len(new_list)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        final_length = 0

        for pos in range(len(s)):
            final_length = get_next_repeat(s[pos::]) if get_next_repeat(s[pos::]) > final_length else final_length

        return final_length


string = 'dvdf'
print(Solution().lengthOfLongestSubstring(string))
