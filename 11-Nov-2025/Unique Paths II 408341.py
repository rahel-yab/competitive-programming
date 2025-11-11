# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid) , len(obstacleGrid[0])
        
        def inbound(r , c):
            return 0 <= r < n and 0 <= c < m
        
        memo = {}
        def dp(i , j):
            state = (i , j)
            if state in memo:
                return memo[state]

            if i > n or j > m:
                return 0
            
            if i == n-1 and j == m-1 and obstacleGrid[i][j] != 1:
                return 1
            
            right , down = 0 , 0
            if inbound(i , j+1 ) and obstacleGrid[i][j+1] != 1:
                right = dp(i , j+1)
            if inbound(i+1 , j) and obstacleGrid[i+1][j] != 1:
                down = dp(i+1 , j)
            
            memo[state] = right + down
            return memo[state]
        
        return dp(0 , 0) if obstacleGrid[0][0] != 1 else 0
            
