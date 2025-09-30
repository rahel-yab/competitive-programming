# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def dp(i, j):
            if i >= len(triangle):
                return 0
                
            if j > i or j < 0:
                return float("inf")
            
            return triangle[i][j]+ min(dp(i+1,j), dp(i+1,j+1))
        
        return dp(0,0)