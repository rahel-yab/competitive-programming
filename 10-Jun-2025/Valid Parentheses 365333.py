# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        mapp = { '(':')', '[':']', '{':'}'}
        stack = []
        for i in s:
            if not stack and i not in mapp:
                return False
            if i not in mapp:
                if stack:
                    if mapp[stack.pop()] != i:
                        return False
            else:
                stack.append(i)
        
        return not stack