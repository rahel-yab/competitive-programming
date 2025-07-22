# Problem: Matrix Diagonal Sum - https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        summ = 0
        for r in range(n):
            for c in range(n):
                if r==c or (r + c) == n-1:
                    summ += mat[r][c]
        return summ