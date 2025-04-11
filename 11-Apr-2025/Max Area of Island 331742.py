# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        row = len(grid)
        col = len(grid[0])
        visited = []
        ans = 0
        def inbound(r,c):
            if 0 <= r < row and 0 <= c < col:
                return True
            return False
        def dfs(r,c):
            nonlocal ans
            visited.append((r,c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if inbound(nr,nc) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                    ans += 1
                    dfs(nr,nc)
                
            return ans
        area = []
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    ans = 1
                    area.append(dfs(r,c))                  
                else:
                    area.append(0)
        return max(area)