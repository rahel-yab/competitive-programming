# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        ind = 0
        for i in range(1,len(nums)):
            while nums[i] != nums[ind]:
                ind += 1
                nums[ind] = nums[i]
        nums = nums[:ind+1]
        return  len(nums)
        
        
    