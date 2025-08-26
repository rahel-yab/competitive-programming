# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return -1

        drns = [(0,1) , (0,-1) , (1,0), (-1,0) , (1,1) , (-1,-1), (1,-1) , (-1,1)]

        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
        
        
        visited = set()
        q= deque()
        q.append((0,0,1))
        visited.add((0,0))

        while q:
            r , c , l = q.popleft()
            
            if r == row-1 and c == col-1:
                return l
            
            for dr , dc in drns:
                nr = r + dr
                nc = c + dc
                if inbound(nr,nc) and (nr,nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr,nc))
                    q.append((nr,nc,l+1))
                
        return -1