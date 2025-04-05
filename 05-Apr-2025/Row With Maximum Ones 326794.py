# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        maxx = 0
        curr_row = 0
        for r in range(row):
            count = 0
            for c in range(col):
                if mat[r][c] == 1:
                    count += 1
            if count > maxx:
                maxx = count
                curr_row = r
        return [curr_row, maxx]