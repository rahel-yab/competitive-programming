# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen = set()
        left = 0
        right = 0
        maxx = 0
        summ = 0
        while right < n:
            while right - left + 1 > k or nums[right] in seen:
                seen.discard(nums[left])
                summ -= nums[left]
                left += 1
                
                
            seen.add(nums[right])
            summ += nums[right]
            if len(seen) == k:
                maxx = max(maxx , summ)
            right += 1
        return maxx
            
