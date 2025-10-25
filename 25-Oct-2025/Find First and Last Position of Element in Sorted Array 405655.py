# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def start(l, r):
            while l <= r:
                mid = (l+r) //2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] == target:
                    if (mid > 0 and nums[mid-1] != target) or mid == 0 :
                        return mid
                    else:
                        r = mid - 1
                else:
                    r = mid -1
            return -1 
        
        def end(l , r):
            while l <= r:
                mid = (l+r) //2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] == target:
                    if (mid < n-1 and nums[mid+1] != target) or mid == n-1:
                        return mid
                    else:
                        l = mid + 1
                else:
                    r = mid -1
            return -1 
        
        low , high = 0 , len(nums) -1 
        s = start(low , high)
        e = end(low , high)
        return [s, e]