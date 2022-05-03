# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                # A profit. Keep L in place and move R regardless
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # Move L to the new low point
                left = right

            right += 1

        return max_profit
