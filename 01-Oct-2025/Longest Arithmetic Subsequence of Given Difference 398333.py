# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = defaultdict(int)
        maxx = float('-inf')
        for num in arr:
            prev = num - difference
            memo[num] = memo[prev] + 1
            maxx = max(maxx, memo[num])
        
        return maxx
