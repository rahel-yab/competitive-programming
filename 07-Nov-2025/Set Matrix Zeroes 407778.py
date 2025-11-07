# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        def set_zero(i , j):
            for k in range(m):
                matrix[i][k] = 0
            for k in range(n):
                matrix[k][j] = 0
        
        zeroes = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeroes.append([i , j])
        
        for r , c in zeroes:
            set_zero(r , c)

    