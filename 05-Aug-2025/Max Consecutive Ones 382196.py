# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        maxx = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                left = right + 1
            maxx = max(maxx , right-left+1)
        return maxx