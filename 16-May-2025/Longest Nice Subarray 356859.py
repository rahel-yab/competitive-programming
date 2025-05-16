# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        left  = 0
        bit = 0
        for right in range(len(nums)):
            while bit & nums[right] != 0:
                bit ^= nums[left]
                left += 1
            bit |= nums[right]
            maxi = max(maxi,right-left+1)
        return maxi