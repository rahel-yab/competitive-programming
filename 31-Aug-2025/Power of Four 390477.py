# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power(num):
            if num == 1:
                return True
            if num == 0:
                return False
            if num % 4 != 0:
                return False
            return power(num//4)
        
        
        return power(n)
