# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        size = n * n * 4  
        parent = [i for i in range(size)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY  
      
        def index(row, col, triangle):
            return (row*n + col)*4 + triangle  

        for row in range(n):
            for col in range(n):
                curr = index(row, col, 0)
                if grid[row][col] == "/":
                    union(curr + 0, curr + 3)  
                    union(curr + 1, curr + 2)  
                elif grid[row][col] == "\\":
                    union(curr + 0, curr + 1) 
                    union(curr + 2, curr + 3)  
                else:
                    union(curr + 0, curr + 1)
                    union(curr + 1, curr + 2)
                    union(curr + 2, curr + 3)
                if row > 0:  
                    union(curr + 0, index(row - 1, col, 2))
                if col > 0: 
                    union(curr + 3, index(row, col - 1, 1))
        
        count = 0
        for i in range(size):
            if parent[i] == i: 
                count += 1
        return count

        