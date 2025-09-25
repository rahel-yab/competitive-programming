# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, total):
            state = (i,total)
            if state in memo:
                return memo[state]
            
            if i >= len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            memo[state] = dp(i+1,total+nums[i]) + dp(i+1, total-nums[i])
            return memo[state]
        
        print(memo)
        return  dp(0,0)
            