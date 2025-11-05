# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n:
            prev = n & 1
            n >>= 1
            if prev == 1 and n & 1:
                return False
            if prev == 0 and n & 1 == 0:
                return False

        return True
