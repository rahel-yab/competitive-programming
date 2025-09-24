# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dp(i):
            if memo[i] != -1:
                return memo[i]

            memo[i] = 1 
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    memo[i] = max(memo[i], dp(j) + 1)
            return memo[i]

        return max(dp(i) for i in range(len(nums)))