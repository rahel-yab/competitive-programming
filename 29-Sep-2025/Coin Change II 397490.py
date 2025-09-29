# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}
        def dp(i, summ):
            state = (i,summ)
            if state in memo:
                return memo[state]
            if i >= len(coins):
                return 0
            
            if summ > amount:
                return 0
            if summ == amount:
                return 1

            memo[state] = dp(i+1, summ) + dp(i, summ+coins[i])
            return memo[state]
        
        return dp(0,0)