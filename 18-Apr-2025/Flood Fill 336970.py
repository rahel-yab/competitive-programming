# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0,1), (0,-1),(1,0),(-1,0)]
        row = len(image)
        col = len(image[0])
        def inbound(r,c):
            if 0 <= r< row and 0 <= c < col:
                return True
            return False

        q = deque()
        q.append([sr,sc])
        visited = set()
        visited.add((sr,sc))
        orig_color = image[sr][sc]
        while q:
            a,b = q.popleft()
            image[a][b] = color
            for dr,dc in directions:
                nr = a + dr
                nc = b + dc
                if inbound(nr,nc) and image[nr][nc] == orig_color and (nr,nc) not in visited :
                    q.append([nr,nc])
                    visited.add((nr,nc))
        return image

