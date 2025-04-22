# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0,1),(0,-1),(1,0),(-1,0), (-1,-1), (-1,1),(1,-1),(1,1)]
        row = len(board)
        col = len(board[0])
        visited = set()
        
        def inbound(r,c):return 0 <= r < row and 0 <= c < col  
    
        def dfs(r,c):
            visited.add((r,c))
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return board
            count = 0
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if inbound(nr,nc) and (nr,nc) not in visited:
                    if board[nr][nc] == 'M':
                        count += 1
            if count:
                board[r][c] = str(count)
            else:
                board[r][c] = 'B'
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if inbound(nr,nc) and (nr,nc) not in visited:
                        if board[nr][nc] == 'E':
                            dfs(nr,nc)
        

        r,c = click
        dfs(r,c)

        return board