# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}

        def dp(r,c):
            state = (r,c)
            if state in memo:
                return memo[state]
            
            if r >= m or c >= n:
                return 0
            
            if r == m -1 and c == n-1:
                return 1


            memo[state] = dp(r+1,c) + dp(r,c+1)
            return memo[state]
        
        return dp(0,0)
            

