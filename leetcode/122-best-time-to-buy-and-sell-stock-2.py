from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_index = len(prices) - 1
        for index, value in enumerate(prices):
            if index == max_index:
                return profit
            if prices[index + 1] > value:
                profit += prices[index + 1] - value


prices1 = [1,2,3,4,5]
print(Solution().maxProfit(prices1))
