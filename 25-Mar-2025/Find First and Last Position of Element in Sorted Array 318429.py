# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def low(nums):
            low = 0
            high = len(nums)-1
            while low <= high:
                mid = (low + high)//2
                if nums[mid] < target:
                    low = mid + 1
                if nums[mid] >= target:
                    high = mid -1
            if low < len(nums) and nums[low] == target:
                return low
            return -1
        def high(nums):
            low = 0
            high = len(nums)-1
            while low <= high:
                mid = (low + high)//2
                if nums[mid] <= target:
                    low = mid + 1
                if nums[mid] > target:
                    high = mid -1
            if high > -1 and nums[high] == target:
                    return high
            return -1
        first = low(nums)
        last = high(nums)
        return [first,last]