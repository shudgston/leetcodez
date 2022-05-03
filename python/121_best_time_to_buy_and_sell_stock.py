# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]

            if profit < 0:
                # A loss, move ahead
                left += 1
                right += 1
            else:
                # A profit
                max_profit = max(max_profit, profit)
                # Keep L where it is and move R
                right += 1

        return max_profit
