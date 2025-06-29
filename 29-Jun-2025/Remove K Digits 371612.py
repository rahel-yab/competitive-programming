# Problem: Remove K Digits - https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and k and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)

        while k:
            if stack:
                stack.pop()
                k -= 1
        ans = ''.join(stack).lstrip('0')
        return ans or '0'


