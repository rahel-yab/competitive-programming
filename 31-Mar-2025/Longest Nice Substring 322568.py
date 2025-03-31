# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def check(s):
            if not s:  
                return ''
            
            _set = set(s)  
            for i in range(len(s)):
                ch = s[i]
            
                if ch.swapcase() not in _set:
                    left = check(s[:i])
                    right = check(s[i+1:])
                   
                    return left if len(left) >= len(right) else right
            
            return s 

        return check(s)

        
        
        