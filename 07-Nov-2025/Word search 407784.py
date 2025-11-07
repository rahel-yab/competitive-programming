# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n , m = len(board) , len(board[0])
        def inbound(r , c):
            return 0 <= r < n and 0 <= c < m
        
        drns = [(0 , 1) , (0, -1) , (1, 0) , (-1, 0)]
        
        visited = set()
        def dfs(r , c, i):
            visited.add((r , c))
            if i >= len(word) - 1:
                return True
            
            for dr , dc in drns:
                nr , nc = r + dr , c + dc
                if inbound(nr , nc) and (nr , nc) not in visited and board[nr][nc] == word[i+1]:
                    if dfs(nr , nc , i+1):
                        return True
            
            visited.remove((r , c))

            return False
          
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0] and (r , c) not in visited:
                    if dfs(r , c , 0):
                        return True
        return False

