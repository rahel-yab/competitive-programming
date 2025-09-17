# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            lcm = nums[i]
            if lcm == k:
                ans += 1
            for j in range(min(i+1, n), n):
                lcm = math.lcm(lcm, nums[j])
                if lcm == k:
                    ans += 1
        
        return ans
