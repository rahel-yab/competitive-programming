# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row = len(mat)
        col = len(mat[0])
        
        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col
        
        q = deque()
        visited = set()
        
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    q.append((r, c, 0))
                    visited.add((r, c))
        
        while q:
            a, b, length = q.popleft()
            for dr, dc in directions:
                nr = a + dr
                nc = b + dc
                if inbound(nr, nc) and (nr, nc) not in visited and mat[nr][nc] == 1:
                    mat[nr][nc] = length + 1
                    q.append((nr, nc, length + 1))
                    visited.add((nr, nc))
        
        return mat
