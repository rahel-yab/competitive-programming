# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        in_arr=set()
        summ, maxSum, l, Len=0, 0, 0, 0 
        for r, x in enumerate(nums):
            summ+=x
            while l<r and (Len>k-1 or x in in_arr):
                in_arr.remove(nums[l])
                summ -=nums[l]
                l+=1
                Len-=1
            in_arr.add(x)
            Len+=1
            if Len==k:
                maxSum=max(maxSum, summ)
        return maxSum
        
