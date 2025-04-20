# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row = len(isWater)
        col = len(isWater[0])
        directions = [(0,1),(0,-1), (1,0), (-1,0)]
        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
        
        visited = set()
        q = deque()
        for r in range(row):
            for c in range(col):
                if isWater[r][c] == 1:
                    isWater[r][c] = 0
                    q.append([r,c,0])
                    visited.add((r,c))
        
        while q:
            a , b, length = q.popleft()
            for dr,dc in directions:
                nr = a + dr
                nc = b + dc
                if inbound(nr,nc) and (nr,nc) not in visited and isWater[nr][nc] == 0:
                    isWater[nr][nc] = length + 1
                    q.append([nr,nc,length + 1])
                    visited.add((nr,nc))
        return isWater



        