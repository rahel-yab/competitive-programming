# Problem: N-Queens II - https://leetcode.com/problems/n-queens-ii/description/

class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        mat = [['.'] * n for _ in range(n)]
        directions = [(0, 1), (1, 1), (1, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1)]

        def check(row, col):
            for dr, dc in directions:
                r, c = row, col
                while 0 <= r < n and 0 <= c < n:
                    if mat[r][c] == 'Q':
                        return False
                    r += dr
                    c += dc
            return True

        def backtrack(row):
            if row == n:
                res.append([''.join(mat[i]) for i in range(n)])
                return
            for col in range(n):
                if check(row, col):
                    mat[row][col] = 'Q'
                    backtrack(row + 1)
                    mat[row][col] = '.'

        backtrack(0)
        return len(res)