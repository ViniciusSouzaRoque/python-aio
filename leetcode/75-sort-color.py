from typing import List


def sort_list(nums):
    current_id = 0

    for position in range(len(nums)):
        for index, color in enumerate(nums):
            if index == current_id:
                continue
            if color > nums[current_id]:
                nums[current_id], nums[index] = nums[index], nums[current_id]
        current_id += 1

    return nums


def update_positions(nums: List[int]):
    print(int(len(nums)/2))

    for index, value in enumerate(nums):
        if value == 0:
            nums.insert(0, nums.pop(index))
        if value == 2:
            nums.insert(len(nums) + 1,  nums.pop(index))
        if value == 1 and index != len(nums) and nums[index + 1] == 0:
            nums[index], nums[index+1] = nums[index+1], nums[index]

    return nums

test_list = [1, 2, 0, 3]
print(update_positions(test_list))