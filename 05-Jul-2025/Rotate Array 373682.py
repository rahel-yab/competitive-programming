# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution(object):  
    def rotate(self, nums: List[int], k: int) -> None:  
        n = len(nums)  
        k = k % n  
        res = [0] * n  
        res[:k] = nums[n-k:]  
        res[k:] = nums[:n-k]  

        for i in range(n):  
            nums[i] = res[i]
        return nums
        