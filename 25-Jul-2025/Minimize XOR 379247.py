# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits1 = [0 for _ in range(32)]

        for i in range(32):
            if num1 & 1:
                bits1[i] = 1
            num1 >>= 1

        count = 0
        for i in range(32):
            if num2 & 1:
                count += 1
            num2 >>= 1

        ans = 0
        for i in range(31, -1 , -1):
            if bits1[i] == 1 and count:
                ans += 1 << i
                count -= 1
        
        
        for i in range(32):
            if count and bits1[i] == 0:
                ans += 1 << i
                count -= 1 
        
        return ans