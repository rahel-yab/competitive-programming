# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        num = x ^ y
        while num > 0:
            if num & 1:
                count += 1
            num >>= 1
        return count