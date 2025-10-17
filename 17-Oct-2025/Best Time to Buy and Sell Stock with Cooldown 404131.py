# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: return 0
        b = [float("-inf")] * n
        s = [0] * n
        for i in range(n):
            s[i] = max(s[i - 1], prices[i] + b[i - 1])
            b[i] = max(b[i - 1], s[i - 2] - prices[i])
        return s[-1]