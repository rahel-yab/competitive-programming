# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            gcdd = 0
            for j in range(i,n):
                gcdd = gcd(gcdd , nums[j])
                if gcdd == k:
                    ans += 1
        return ans
