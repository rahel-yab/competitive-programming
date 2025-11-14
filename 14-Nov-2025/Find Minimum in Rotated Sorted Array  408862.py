# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) -1 

        while low < high:
            mid = (low+high) //2
            if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return nums[mid]
            
            elif nums[-1] < nums[mid]:
                low = mid+1
            else:
                high = mid
        
        return nums[high]
