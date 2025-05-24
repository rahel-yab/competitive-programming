# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        bit = num ^ num
        shift = 0    
        while num:
            if not (num & 1): 
                bit |= (1 << shift)
            num >>= 1
            shift += 1       
        return bit