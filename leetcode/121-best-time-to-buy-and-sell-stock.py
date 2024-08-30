from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            possible_profit = price - min_price
            max_profit = max(max_profit, possible_profit)

        return max_profit

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))

