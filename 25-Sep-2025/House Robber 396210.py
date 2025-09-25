# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums)+2)
        def dp(i):
            if memo[i] != -1:
                return memo[i]
            if i >= len(nums):
                return 0
            
            memo[i] = max(nums[i]+ dp(i+2), dp(i+1))
            return memo[i]
        return dp(0)
    