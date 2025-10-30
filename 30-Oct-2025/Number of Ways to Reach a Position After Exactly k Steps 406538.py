# Problem: Number of Ways to Reach a Position After Exactly k Steps - https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        mod = 10**9 + 7
        val = endPos -startPos
        if abs(val) > k:
            return 0
        if k == val:
            return 1
        if (k - val) % 2 != 0:
            return 0
        
        left = (k - val) // 2
        # minn = min(val , k)
        ans = factorial(k)//(factorial(left) * (factorial(k - left)))
        return ans % mod