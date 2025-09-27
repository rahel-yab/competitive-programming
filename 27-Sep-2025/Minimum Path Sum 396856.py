# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])

        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
        
        memo = {}
        def dp(r, c):
            state = (r,c)
            if state in memo:
                return memo[state]
            if r == row -1 and c == col-1:
                return 0

            right, down = float('inf') , float('inf')

            if inbound(r+1,c):
                down = grid[r+1][c]+ dp(r+1,c)
            if inbound(r, c+1):
                right = grid[r][c+1] + dp(r,c+1)
        
            memo[state] = min(down, right)
            return memo[state]

        return grid[0][0] + dp(0,0)
