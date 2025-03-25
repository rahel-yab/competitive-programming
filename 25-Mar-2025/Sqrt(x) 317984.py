# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        s = 0
        while low <= high:
            mid = (low + high)//2
            target = mid * mid
            if x >= target:
                s = mid
                low = mid + 1
            else:
                high = mid -1
                
        return s