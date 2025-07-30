# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        dictt = {}
        maxx = 0
        left = 0
        count = 0
        right = 0
        while right < len(s)-1 and left < len(s):
            if s[right] == s[right+1]:
                count += 1
            while count > 1:
                if s[left] == s[left+1]:
                    count -= 1
                left += 1
            maxx = max(maxx, right-left+2)
            right += 1
        return maxx


            