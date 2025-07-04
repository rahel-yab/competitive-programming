# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:  
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxx = 0
        left = 0
        curr = 0
        for right in range(len(t)):
            curr += abs(ord(s[right]) - ord(t[right]))
            while curr > maxCost:
                curr -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            maxx = max(maxx , right - left + 1)
        return maxx
