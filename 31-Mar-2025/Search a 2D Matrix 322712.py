# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            val = matrix[mid // cols][mid % cols]  

            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
