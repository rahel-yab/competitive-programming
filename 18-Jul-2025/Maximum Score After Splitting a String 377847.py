# Problem: Maximum Score After Splitting a String - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxx = float('-inf')
        for i in range(1,len(s)):
            ones = s[i:].count('1')
            zero = s[:i].count('0')
            maxx = max(maxx, ones + zero)
        return maxx

        