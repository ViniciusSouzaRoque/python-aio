from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        end_list = []
        max_position = len(nums) - 1

        start_value = None

        for index, step in enumerate(nums):
            current_value = step
            if start_value is None:
                start_value = step
                current_value = step

            if index == max_position or current_value + 1 != nums[index+1]:
                if start_value == current_value:
                    end_list.append(f"{start_value}")
                else:
                    end_list.append(f"{start_value}->{current_value}")
                start_value = None

        return end_list


input_list = [0,1,2,4,5,7]

solution = Solution()

print(solution.summaryRanges(input_list))